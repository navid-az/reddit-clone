let commentForm = document.getElementById("comment-form");
let commetFormSubmitBtn = document.getElementById("comment-submit-btn");

commentForm.addEventListener("keydown", () => {
  commentForm.style.border = "1px solid var(--orange)";
  commetFormSubmitBtn.style.background = "var(--orange)";
});

// open and close reply form
let replyForms = document.querySelectorAll(`[id^="reply-to-"]`);
replyForms.forEach((id) => {
  id.style.display = "none";
});
const openReplyForm = (id) => {
  let replyForm = document.getElementById(`reply-to-${id}`);
  if (replyForm.style.display == "block") {
    replyForm.style.display = "none";
  } else if (replyForm.style.display == "none") {
    replyForm.style.display = "block";
  }
};
