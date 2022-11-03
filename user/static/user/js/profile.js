let userPostsWrapper = document.getElementById("user-posts-wrapper");
let userCommentsWrapper = document.getElementById("user-comments-wrapper");
let showPostsBtn = document.querySelector(".show-posts");
let showCommentsBtn = document.querySelector(".show-comments");
let username = document.querySelector(
  ".profile-image-wrapper > .user-tag"
).innerHTML;

const changeView = (btn) => {
  if (window.location.href == `http://127.0.0.1:8000/${username}/profile/`) {
    if (btn == 0) {
      showPostsBtn.style.background = "#FF3F18";
      showPostsBtn.style.color = "#FFFF";
      showCommentsBtn.style.background = "unset";
      showCommentsBtn.style.color = "rgb(215, 215, 215)";

      userCommentsWrapper.style.opacity = "0";
      setTimeout(() => {
        userCommentsWrapper.classList.add("d-none");
        userPostsWrapper.classList.remove("d-none");
      }, 200);
      setTimeout(() => {
        userPostsWrapper.style.opacity = "1";
      }, 500);
    } else {
      showCommentsBtn.style.background = "#FF3F18";
      showCommentsBtn.style.color = "#FFFF";
      showPostsBtn.style.background = "unset";
      showPostsBtn.style.color = "rgb(215, 215, 215)";

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
    window.location.replace(`http://127.0.0.1:8000/${username}/profile/`);

    // this will send btn value to the profile page
    localStorage.setItem("BTN", btn);
  }
};

if (window.location.href == `http://127.0.0.1:8000/${username}/profile/`) {
  var buttonCode = localStorage.getItem("BTN");
  changeView(buttonCode);
}
