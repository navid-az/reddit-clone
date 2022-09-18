let userPostsWrapper = document.getElementById("user-posts-wrapper");
let userCommentsWrapper = document.getElementById("user-comments-wrapper");

const changeView = (btn) => {
  if (btn == 0) {
    userCommentsWrapper.style.opacity = "0";
    setTimeout(() => {
      userCommentsWrapper.classList.add("d-none");
      userPostsWrapper.classList.remove("d-none");
    }, 200);
    setTimeout(() => {
      userPostsWrapper.style.opacity = "1";
    }, 500);
  } else {
    userPostsWrapper.style.opacity = "0";
    setTimeout(() => {
      userPostsWrapper.classList.add("d-none");
      userCommentsWrapper.classList.remove("d-none");
    }, 200);
    setTimeout(() => {
      userCommentsWrapper.style.opacity = "1";
    }, 500);
  }
};

changeView(0);
