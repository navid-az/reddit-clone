let userPostsWrapper = document.getElementById("user-posts-wrapper");
let userCommentsWrapper = document.getElementById("user-comments-wrapper");

const changeView = (btn) => {
  if (window.location.href == "http://127.0.0.1:8000/u/reddit/profile/") {
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
  } else {
    window.location.replace("http://127.0.0.1:8000/u/reddit/profile/");

    // this will send btn value to the profile page
    localStorage.setItem("BTN", btn);
  }
};

if (window.location.href == "http://127.0.0.1:8000/u/reddit/profile/") {
  var buttonCode = localStorage.getItem("BTN");
  changeView(buttonCode);
}
