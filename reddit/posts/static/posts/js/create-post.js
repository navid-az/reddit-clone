let postTypeBtn = document.querySelectorAll("button");
let postInputs = document.querySelectorAll(".field");

function postType(i) {
  postInputs.forEach((input) => {
    input.style.display = "none";
  });
  postInputs[i].style.display = "block";

  //   if (this.innerHTML == "text") {
  //     console.log("this is a text field");
  //   } else if (this.innerHTML == "video") {
  //     console.log("this is a video field");
  //   } else if (this.innerHTML == "image") {
  //     console.log("this is a image field");
  //   }
}
postType(0);
