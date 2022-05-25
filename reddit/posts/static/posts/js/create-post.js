let postTypeBtn = document.querySelectorAll("button");
let postInputs = document.querySelectorAll(".field");

// choose between post type options
function postType(i) {
  postInputs.forEach((input) => {
    input.style.display = "none";
  });
  postInputs[i].style.display = "block";
}
postType(0);

// create post tab will open up
// $.ajax({
//   type: "GET",
//   url: "posts/post-tab/",
//   success: function (response) {
//     console.log("success", response);
//   },
//   error: function (error) {
//     console.log("error:", error);
//   },
// });
