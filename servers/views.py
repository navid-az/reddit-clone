from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import Server, ServerFollow, ServerPostTag, ServerRule, ServerUserTag, ServerModerator
from .forms import AddModeratorForm, CreateServerForm, CreatePostTagForm, CreateUserTagForm, CreateRuleForm, UpdateModeratorPermissionsForm, LimitUserForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
import itertools
from django.db.models import Count
from django.db.models.functions import TruncDate
from datetime import timedelta, datetime
from django.utils import timezone
import pytz

from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
class ServerView(View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        posts = server.posts.all()
        post_tags = server.post_tags.all()
        user_tags = server.user_tags.all()
        
        if request.user.is_authenticated:
            is_limited = server.limited_users.filter(server=server, user=request.user)
            is_following = ServerFollow.objects.filter(server=server, user=request.user)
            current_date = datetime.now(pytz.utc)

            for x in is_limited:
                ban_for = timedelta(days=int(x.duration))
                if x.duration != 'permanent' and current_date >= x.created + ban_for:
                    x.delete()
                else:
                    print('there is still time left','%%%%%%%')
            if user_tags.filter(user=request.user).exists():
                current_user_tag = user_tags.get(user=request.user)
            else:
                current_user_tag = None
            return render(request, 'servers/server.html', {'server':server, 'posts':posts, 'is_following':is_following, 'is_limited':is_limited, 'user_tags':user_tags, 'post_tags':post_tags, 'current_user_tag':current_user_tag})
        return render(request, 'servers/server.html', {'server':server, 'posts':posts, 'user_tags':user_tags, 'post_tags':post_tags})

class ServerFollowView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        relation = server.followers.filter(server=server, user=request.user)
        limitedUser = server.limited_users.filter(server=server, user=request.user)
        
        if relation.exists():
            relation.delete()
        elif limitedUser.exists():
            messages.error(request,'شما از فعالیت در این سرور محدود شدید')
        else:
            ServerFollow(server=server, user=request.user).save()
        return redirect('servers:server', server.tag)

class CreateServerView(LoginRequiredMixin, View):
    form_class = CreateServerForm

    def post(self, request):
        create_form = self.form_class(request.POST)

        if create_form.is_valid():
            saved_form = create_form.save(commit=False)
            saved_form.creator = request.user
            saved_form.name = saved_form.tag.capitalize()
            saved_form.save()
            messages.success(request, '!سرور با موفقیت ایجاد شد')
            return redirect('home:home')
        messages.error(request, '!این نام سرور قبلا ثبت شده')
        return redirect('home:home')

class ServerModeratingView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        moderator = server.moderator_of.filter(user=request.user, server=server)
        if moderator.exists():
            return render(request, 'servers/moderating-page.html', {"server":server})
        messages.warning(request, 'شما مدیر این سرور نیستید')
        return redirect('home:home')
class ServerInsightsView(View):
    form_class = LimitUserForm

    def get(self, request, server_tag):
        limit_user = self.form_class()         
        server = Server.objects.get(tag=server_tag)
        server_reports = server.reports.all()

        today = timezone.now()
        last_day = timezone.now() - timedelta(1)
        daily_follow_count_icon = daily_post_count_icon = ''

        today_post_count = server.posts.filter(created__date=today).count()
        today_follow_count = server.followers.filter(created__date=today).count()
        last_day_post_count = server.posts.filter(created__date=last_day).count()
        last_day_follow_count = server.followers.filter(created__date=last_day).count()
        server_numbers = [today_post_count, today_follow_count]
        
        if today_post_count > last_day_post_count:
            daily_post_count_icon = 'higher'
        elif today_post_count < last_day_post_count:
            daily_post_count_icon = 'lower'
        else:
            daily_post_count_icon = 'same'

        if today_follow_count > last_day_follow_count:
            daily_follow_count_icon = 'higher'
        elif today_follow_count < last_day_follow_count:
            daily_follow_count_icon = 'lower'
        else:
            daily_follow_count_icon = 'same'

        # chart
        days_ago_30=today-timedelta(days=30)
        server_posts = server.posts.filter(created__date__range=(days_ago_30.date(),today.date()))
        server_followers = server.followers.filter(created__date__range=(days_ago_30.date(),today.date()))
        post_daily_count = list(server_posts.annotate(date=TruncDate('created')).values('date').annotate(dailycount=Count('date')).order_by())
        server_follow_daily_count = list(server_followers.annotate(date=TruncDate('created')).values('date').annotate(dailycount=Count('date')).order_by())

        for value in post_daily_count:
            value['date'] = str(value['date'])

        for value in server_follow_daily_count:
            value['date'] = str(value['date']) 
        return render(request, 'servers/insights.html', {'limit_user':limit_user, 'server':server, 'server_reports':server_reports, 'post_daily_count': post_daily_count, 'server_follow_daily_count':server_follow_daily_count, 'daily_post_count_icon':daily_post_count_icon, 'daily_follow_count_icon':daily_follow_count_icon, 'server_numbers':server_numbers})

    def post(self, request, server_tag):
        limit_user = self.form_class(request.POST)
        server = Server.objects.get(tag=server_tag)
        user = User.objects.get(id=request.POST['user'])
        server_limited_users = server.limited_users.filter(user=user)

        if limit_user.is_valid() and not server_limited_users.exists():
            limit = limit_user.save(commit=False)
            limit.server = server
            limit.save()
        else:
            messages.error(request, 'این کاربر قبلا از این سرور محدود شده.')
        return redirect('servers:server-insights', server_tag)       
class ServerDeleteReportView(LoginRequiredMixin, View):
    def get(self, request, server_tag, report_id):
        server = Server.objects.get(tag=server_tag)
        report = server.reports.filter(id=report_id)
        moderator = server.moderator_of.get(user=request.user)
        permission = server.permissions.filter(moderator=moderator, allow_delete_report=True)
        if permission.exists():
            report.delete()
            return redirect('servers:server-insights', server_tag)
        messages.error(request, 'شما اجازه حذف گزارشات را ندارید.') 
        return redirect('servers:server-insights', server_tag)
class TagsAndFlairsView(LoginRequiredMixin, View):
    form_class = CreatePostTagForm
    form_class_2 = CreateUserTagForm

    def setup(self, request, *args, **kwargs):
        self.server = get_object_or_404(Server, tag=kwargs['server_tag'])
        self.moderator = self.server.moderator_of.filter(user=request.user, server=self.server)
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        create_post_tag_form = self.form_class(prefix='post-tag')
        create_user_tag_form = self.form_class_2(prefix='user-tag')
        
        server_post_tags = self.server.post_tags.all()
        server_user_tags = self.server.user_tags.all()
        if self.moderator.exists():
            return render(request, 'servers/tags-flairs.html', {"server":self.server, "server_post_tags":server_post_tags, "server_user_tags":server_user_tags, "create_post_tag_form":create_post_tag_form, "create_user_tag_form":create_user_tag_form})
        messages.warning(request, 'شما مدیر این سرور نیستید')
        return redirect('home:home')

    def post(self, request, server_tag):
        create_post_tag_form = self.form_class(request.POST, prefix='post-tag')
        create_user_tag_form = self.form_class_2(request.POST, prefix='user-tag')

        moderator = self.moderator.first()
        permission = moderator.permissions.filter(server=self.server, allow_create_tag=True)
        if permission.exists():
            if create_post_tag_form.is_valid():
                created_post_tag = create_post_tag_form.save(commit=False)
                created_post_tag.server = self.server
                created_post_tag.creator = request.user
                created_post_tag.save()
                return redirect('servers:server-tags-and-flairs', server_tag)
            elif create_user_tag_form.is_valid():
                created_user_tag = create_user_tag_form.save(commit=False)
                created_user_tag.server = self.server
                created_user_tag.creator = request.user
                created_user_tag.save()
                return redirect('servers:server-tags-and-flairs', server_tag)
            messages.error(request, 'تگ بدون نام مجاز نیست')
            return redirect('servers:server-tags-and-flairs', server_tag)
        messages.error(request, 'شما نمیتوانید تگ ایجاد کنید')
        return redirect('servers:server-tags-and-flairs', server_tag)
class DeleteTagsAndFlairsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_tag = ServerPostTag.objects.filter(pk=kwargs['tag_id'])
        user_tag = ServerUserTag.objects.filter(pk=kwargs['tag_id'])

        server = Server.objects.get(tag=kwargs['server_tag'])
        moderator = server.moderator_of.get(user=request.user)
        permission = moderator.permissions.filter(server=server, allow_delete_tag=True)
        if permission.exists():
            if post_tag.exists():
                post_tag.delete()
                return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
            elif user_tag.exists():
                user_tag.delete()
                return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
        messages.error(request, 'شما اجازه حذف تگ در این سرور را ندارید')
        return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
class RulesView(LoginRequiredMixin, View):
    class_form = CreateRuleForm

    def setup(self, request, *args, **kwargs):
        self.server = get_object_or_404(Server, tag=kwargs['server_tag'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        create_rule_form = self.class_form()

        server_rules = self.server.rules.all()
        moderator = self.server.moderator_of.filter(user=request.user)
        if moderator.exists():
            return render(request, 'servers/rules.html', {"server":self.server, "server_rules":server_rules, "create_rule_form":create_rule_form})
        messages.warning(request, 'شما مدیر این سرور نیستید')
        return redirect('home:home')

    def post(self, request, server_tag):
        create_rule_form = self.class_form(request.POST)

        server_rules = self.server.rules.all()
        moderator = self.server.moderator_of.get(user=request.user)
        permission = moderator.permissions.filter(server=self.server, allow_create_rule=True)
        if permission.exists():
            if create_rule_form.is_valid():
                new_rule = create_rule_form.save(commit=False)
                new_rule.server = self.server
                new_rule.creator = request.user
                new_rule.save()
                return redirect('servers:server-rules', server_tag)
            return render(request, 'servers/rules.html', {"server":self.server, "server_rules":server_rules, "create_rule_form":create_rule_form})
        messages.error(request, 'شما نمیتوانید قانون ایجاد کنید')
        return redirect('servers:server-rules', server_tag)
class DeleteRulesView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        moderator = server.moderator_of.get(user=request.user)
        permission = moderator.permissions.filter(server=server, allow_delete_rule=True)
        if permission.exists():
            rule = ServerRule.objects.filter(pk=kwargs['rule_id'])
            if rule.exists():
                rule.delete()
                return redirect('servers:server-rules', kwargs['server_tag'])
            else:
                messages.error(request, 'فقط مدیر سرور میتواند قانون سرور را حذف کند')
                return redirect('home:home')
        messages.error(request, 'شما اجازه حذف قانون در این سرور را ندارید')
        return redirect('servers:server-rules', kwargs['server_tag'])
class ModeratorSettingsView(LoginRequiredMixin, View):
    form_class = AddModeratorForm

    def get(self, request, server_tag):
        form = self.form_class()
        server = Server.objects.get(tag=server_tag)
        moderators = server.moderator_of.exclude(user=server.creator)
        return render(request, 'servers/moderator-settings.html', {'moderators':moderators, 'server':server, 'form':form})

    def post(self, request, server_tag):
        form = self.form_class(request.POST)
        user = User.objects.get(pk=request.POST.get('user'))
        server = Server.objects.get(tag=server_tag)
        moderators = server.moderator_of.exclude(user=server.creator)
        ServerModerator.objects.get_or_create(user=user)
        moderator = ServerModerator.objects.get(user=user)
        moderator.server.add(server)
        return render(request, 'servers/moderator-settings.html', {'moderators':moderators, 'server':server, 'form':form})
class ModeratorPermissionsView(LoginRequiredMixin, View):
    form_class = UpdateModeratorPermissionsForm

    def setup(self, request, *args, **kwargs):
        self.server = get_object_or_404(Server, tag=kwargs['server_tag'])
        self.moderator = self.server.moderator_of.get(user=kwargs['user_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        permission = self.server.permissions.get(moderator=self.moderator)
        form = self.form_class(instance=permission)
        return render(request, 'servers/moderator-permissions.html', {'server':self.server, 'moderator':self.moderator, 'form':form})
    
    def post(self, request, *args, **kwargs):
        permission = self.server.permissions.get(moderator=self.moderator)
        form = self.form_class(request.POST, instance=permission)
        if form.is_valid():
            updated_permission = form.save(commit=False)
            updated_permission.server = self.server
            updated_permission.moderator = self.moderator
            updated_permission.save()
            messages.success(request, '!دسترسی های مدیر با موفقیت ویرایش شد')
            return redirect('servers:server-moderator-settings', kwargs['server_tag'])
        messages.success(request, 'yes')
        return render(request, 'servers/moderator-permissions.html', {'server':self.server, 'moderator':self.moderator, 'form':form})

def ModeratorSearchAjaxView(request):
    if is_ajax(request=request):
        username = request.POST.get('user')
        users = User.objects.filter(username__icontains=username)
        if len(users) > 0 and len(username) > 0:
            data = []
            for user in users:
                item = {
                    'id':user.id,
                    'username':user.username,
                    'image': str(user.profile.image.url),
                }
                data.append(item)
            response = data
        else:
            response = 'کاربری با این نام یافت نشد'
        return JsonResponse({'data':response})
    return JsonResponse({})
class ChooseServerAjaxView(LoginRequiredMixin, View):
    def get(self, request):
        moderator = ServerModerator.objects.get(user=request.user)
        moderator_servers = moderator.server.all()
        user_servers = itertools.chain(moderator_servers)
        data = []
        for i in user_servers:
            list ={
            'tag':i.tag,
            'name':i.name,
            'about':i.about,
            'server_type':i.server_type
            }
            data.append(list)
        return JsonResponse({'data':data})
class LimitationDoneAjaxView(LoginRequiredMixin, View):
    def get(self, request):
        pass

class ServerSettingsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        return render(request, 'servers/server-settings.html', {"server":server})