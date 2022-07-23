import sys
sys.path.append("..")
from servers.forms import CreateServerForm
from django.utils.decorators import method_decorator

from servers.models import Server

def inject_form(request):
    return {'create_server_form': CreateServerForm()}

def is_moderator(request):
    is_moderator = Server.objects.filter(creator=request.user.id)
    return {'is_moderator': is_moderator}