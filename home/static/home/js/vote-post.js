const votePostForm = document.querySelectorAll(".vote-post-form");

votePostForm.forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const postId = form.id;
    const activeSubmitBtn = document.activeElement;
    const submitBtn = form.querySelectorAll(".vote-wrapper>.vote-btn");
    // const upSubmitBtn = submitBtn[0].getElementsByTagName("img")[0].src;
    // const upSubmitBtn = submitBtn[1].getElementsByTagName("img")[0].src;
    const voteIcon = "http://127.0.0.1:8000/static/svgs/vote.svg";
    const upvotedIcon = "http://127.0.0.1:8000/static/svgs/up-voted.svg";
    const downvotedIcon = "http://127.0.0.1:8000/static/svgs/down-voted.svg";

    // const submitBtnsImg = submitBtn[0].document.getElementsByTagName("img");
    // submitBtn.forEach((btn)=>{const btnImg = btn.getElementsByTagName("img")})
    // const submitBtnImg = activeSubmitBtn.getElementsByTagName("img");
    let voteCounter = document.getElementById(`vote-counter-${postId}`);
    // const downvoteIcon = "http://127.0.0.1:8000/static/svgs/down-vote.svg";
    $.ajax({
      type: "POST",
      url: "/posts/vote/",
      data: {
        csrfmiddlewaretoken: csrf,
        postId: postId,
        voteType: activeSubmitBtn.name,
      },
      success: () => {
        // if (activeSubmitBtn == submitBtn[0]) {
        //   if (submitBtnImg[0].src == upvotedIcon) {
        //     submitBtnImg[0].src = upvoteIcon;
        //     voteCounter.innerHTML--;
        //   } else if (submitBtnImg[0].src == upvotedIcon) {
        //     submitBtnImg[0].src = upvotedIcon;
        //     voteCounter.innerHTML++;
        //   }
        // } else if (activeSubmitBtn.name == submitBtn[1]) {
        //   if (submitBtnImg[0].src == downvotedIcon) {
        //     submitBtnImg[0].src = downvoteIcon;
        //     voteCounter.innerHTML++;
        //   } else if (submitBtnImg[0].src == upvotedIcon) {
        //     submitBtnImg[0].src = downvotedIcon;
        //     voteCounter.innerHTML = voteCounter.innerHTML - 2;
        //   }
        // }
        if (activeSubmitBtn == submitBtn[0]) {
          if (
            submitBtn[1].getElementsByTagName("img")[0].src == downvotedIcon
          ) {
            // voteCounter.innerHTML = voteCounter.innerHTML + 2;
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 2;
            submitBtn[1].getElementsByTagName("img")[0].src = voteIcon;
            submitBtn[0].getElementsByTagName("img")[0].src = upvotedIcon;
          } else if (
            submitBtn[0].getElementsByTagName("img")[0].src == upvotedIcon
          ) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 1;
            submitBtn[0].getElementsByTagName("img")[0].src = voteIcon;
          } else {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 1;
            submitBtn[0].getElementsByTagName("img")[0].src = upvotedIcon;
          }
        } else if (activeSubmitBtn == submitBtn[1]) {
          if (submitBtn[0].getElementsByTagName("img")[0].src == upvotedIcon) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 2;
            submitBtn[0].getElementsByTagName("img")[0].src = voteIcon;
            submitBtn[1].getElementsByTagName("img")[0].src = downvotedIcon;
          } else if (
            submitBtn[1].getElementsByTagName("img")[0].src == downvotedIcon
          ) {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) + 1;
            submitBtn[1].getElementsByTagName("img")[0].src = voteIcon;
          } else {
            voteCounter.innerHTML = Number(voteCounter.innerHTML) - 1;
            submitBtn[1].getElementsByTagName("img")[0].src = downvotedIcon;
          }
        }
      },
      error: (err) => {
        window.location.href = "http://127.0.0.1:8000/accounts/login/";
      },
    });
  });
});
