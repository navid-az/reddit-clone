let tagColorOption = document.querySelectorAll(".tag-color-option");
let postTagPrimaryColorInput = document.getElementById("id_primary_color");
let postTagSecondaryColorInput = document.getElementById("id_secondary_color");
let tagColorOptionsList = [];

const rgb2hex = (rgb) =>
  `#${rgb
    .match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/)
    .slice(1)
    .map((n) => parseInt(n, 10).toString(16).padStart(2, "0"))
    .join("")}`;

tagColorOption.forEach((postTagColor, i) => {
  tagColorOptionsList.push([
    rgb2hex(tagColorOption[i].style.background),
    rgb2hex(tagColorOption[i].style.borderColor),
  ]);
  console.log(tagColorOptionsList);
  postTagColor.addEventListener("click", () => {
    postTagPrimaryColorInput.value = tagColorOptionsList[i][0];
    postTagSecondaryColorInput.value = tagColorOptionsList[i][1];
  });
});
