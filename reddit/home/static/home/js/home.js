// let postsWrapper = document.getElementById("posts-wrapper");
// $.ajax({
//   type: "GET",
//   url: "/hot/",
//   success: function (response) {
//     const data = response.data;
//     console.log(data);
//     data.forEach((post) => {
//       postsWrapper.innerHTML += `
// <div class="post">
//   <div class="post-header">
//     <div class="vote">
//       <img class="upvote" src="{% static 'svgs/up-vote.svg' %}" alt="">
//       <p class="vots-counter">{{post.vote_count}}</p>
//       <img class="upvote" src="{% static 'svgs/down-vote.svg' %}" alt="">
//     </div>
//     <div class="server-info">
//       <div class="post-info">
//         <section>
//           <a class="creator-name" href='{{post.get_profile_page}}'>u/${post.creator} پست شده توسط </a>
//           <a class="server-name" href='{{post.get_absolute_url}}'>r/${post.server}</a>
//         </section>
//         <section>
//           <div class="post-tags"></div>
//           <a href='{{post.get_absolute_url}}'><h3 class="post-title">${post.title}</h3></a>
//         </section>
//       </div>
//       <div class="server-img"><img src="${post.server_image}" alt=""></div>
//     </div>
//   </div>
//   <div class="post-body">
//     {% if post.image %}
//       <img src="${post.image}" alt="">
//     {% elif post.video %}
//       <video controls>
//         <source src="{{post.video.url}}" type="video/mp4">
//       </video>
//     {% elif post.text %}
//       <p>${post.text}</p>
//     {% endif %}
//   </div>

//   <div class="post-footer">
//     <div class="post-items">
//       <div><img class="comment-btn" src="{% static 'posts/svgs/comment.svg' %}" alt="">{{comments_count}}</div>
//       <img class="share-btn" src="{% static 'posts/svgs/share.svg' %}" alt="">
//       <img class="save-btn" src="{% static 'posts/svgs/save.svg' %}" alt="">
//     </div>
//     <div class="post-options">
//       {% if request.user.id == post.creator.id %}
//         <a href="{% url 'posts:delete-post' post.id %}"><img src="{% static 'posts/svgs/trash.svg' %}" alt=""></a>
//         <div id="join-btn"><a href="{% url 'posts:update-post' post.id %}">ویرایش</a></div>
//       {% endif %}

//       <div id="join-btn"><a href="">عضویت</a></div>
//     </div>
//   </div>
// </div>`;
//     });
//     console.log("kir");
//   },
//   error: function (error) {
//     console.log("error", error);
//   },
// });
