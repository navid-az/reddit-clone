const savePostCsrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const savePostForm = document.querySelectorAll(".save-post-form");

savePostForm.forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const postId = form.id;
    const savePostBtnImg = document.getElementById(
      `save-post-btn-img-${postId}`
    );

    $.ajax({
      type: "POST",
      url: "/posts/save/",
      data: {
        csrfmiddlewaretoken: csrf,
        postId: postId,
      },
      success: () => {
        if (
          savePostBtnImg.src ==
          "http://127.0.0.1:8000/static/posts/svgs/save.svg"
        ) {
          savePostBtnImg.src =
            "http://127.0.0.1:8000/static/posts/svgs/saved.svg";
        } else {
          savePostBtnImg.src =
            "http://127.0.0.1:8000/static/posts/svgs/save.svg";
        }
      },
      error: (err) => {
        window.location.href = "http://127.0.0.1:8000/accounts/login/";
      },
    });
  });
});
