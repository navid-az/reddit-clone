const votePostForm = document.querySelectorAll(".vote-post-form");

votePostForm.forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const postId = form.id;

    const activeSubmitBtn = document.activeElement;
    const submitBtn = form.querySelectorAll(".vote-wrapper>.vote-btn");
    const upvoteBtn = submitBtn[0].getElementsByTagName("img")[0];
    const downvoteBtn = submitBtn[1].getElementsByTagName("img")[0];

    const voteIcon = "http://127.0.0.1:8000/static/svgs/vote.svg";
    const upvotedIcon = "http://127.0.0.1:8000/static/svgs/up-voted.svg";
    const downvotedIcon = "http://127.0.0.1:8000/static/svgs/down-voted.svg";

    let voteCounter = document.getElementById(`vote-counter-${postId}`);

    $.ajax({
      type: "POST",
      url: "/posts/vote/",
      data: {
        csrfmiddlewaretoken: csrf,
        postId: postId,
        voteType: activeSubmitBtn.name,
        voteFor: "post",
      },
      success: () => {
        if (activeSubmitBtn == submitBtn[0]) {
          if (downvoteBtn.src == downvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 2;
            downvoteBtn.src = voteIcon;
            upvoteBtn.src = upvotedIcon;
          } else if (upvoteBtn.src == upvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 1;
            upvoteBtn.src = voteIcon;
          } else {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 1;
            upvoteBtn.src = upvotedIcon;
          }
        } else {
          if (upvoteBtn.src == upvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 2;
            upvoteBtn.src = voteIcon;
            downvoteBtn.src = downvotedIcon;
          } else if (downvoteBtn.src == downvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 1;
            downvoteBtn.src = voteIcon;
          } else {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 1;
            downvoteBtn.src = downvotedIcon;
          }
        }
      },
      error: (err) => {
        window.location.href = "http://127.0.0.1:8000/accounts/login/";
      },
    });
  });
});

const voteCommentForm = document.querySelectorAll(".vote-comment-form");

voteCommentForm.forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const commentId = form.id;

    const activeSubmitBtn = document.activeElement;
    const submitBtn = form.querySelectorAll(".vote-wrapper>.vote-btn");
    const upvoteBtn = submitBtn[0].getElementsByTagName("img")[0];
    const downvoteBtn = submitBtn[1].getElementsByTagName("img")[0];

    const voteIcon = "http://127.0.0.1:8000/static/svgs/vote.svg";
    const upvotedIcon = "http://127.0.0.1:8000/static/svgs/up-voted.svg";
    const downvotedIcon = "http://127.0.0.1:8000/static/svgs/down-voted.svg";

    let voteCounter = document.getElementById(`vote-counter-${commentId}`);

    $.ajax({
      type: "POST",
      url: "/posts/vote/",
      data: {
        csrfmiddlewaretoken: csrf,
        commentId: commentId,
        voteType: activeSubmitBtn.name,
        voteFor: "comment",
      },
      success: () => {
        if (activeSubmitBtn == submitBtn[0]) {
          if (downvoteBtn.src == downvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 2;
            downvoteBtn.src = voteIcon;
            upvoteBtn.src = upvotedIcon;
          } else if (upvoteBtn.src == upvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 1;
            upvoteBtn.src = voteIcon;
          } else {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 1;
            upvoteBtn.src = upvotedIcon;
          }
        } else {
          if (upvoteBtn.src == upvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 2;
            upvoteBtn.src = voteIcon;
            downvoteBtn.src = downvotedIcon;
          } else if (downvoteBtn.src == downvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 1;
            downvoteBtn.src = voteIcon;
          } else {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 1;
            downvoteBtn.src = downvotedIcon;
          }
        }
      },
      error: (err) => {
        window.location.href = "http://127.0.0.1:8000/accounts/login/";
      },
    });
  });
});
