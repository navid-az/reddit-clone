let tagColorOption = document.querySelectorAll(".tag-color-option");
let postTagNameInput = document.getElementById("id_post-tag-name");
let userTagNameInput = document.getElementById("id_user-tag-name");
let postTagPrimaryColorInput = document.getElementById(
  "id_post-tag-primary_color"
);
let postTagSecondaryColorInput = document.getElementById(
  "id_post-tag-secondary_color"
);
let userTagPrimaryColorInput = document.getElementById(
  "id_user-tag-primary_color"
);
let userTagSecondaryColorInput = document.getElementById(
  "id_user-tag-secondary_color"
);
let liveTagOverview = document.querySelectorAll(".live-tag-overview");
let tagColorOptionsList = [];
var timeout = setTimeout(function () {}, 0);

const rgb2hex = (rgb) =>
  `#${rgb
    .match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/)
    .slice(1)
    .map((n) => parseInt(n, 10).toString(16).padStart(2, "0"))
    .join("")}`;

// function checkRTL(s) {
//   var ltrChars =
//       "A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02B8\u0300-\u0590\u0800-\u1FFF" +
//       "\u2C00-\uFB1C\uFDFE-\uFE6F\uFEFD-\uFFFF",
//     rtlChars = "\u0591-\u07FF\uFB1D-\uFDFD\uFE70-\uFEFC",
//     rtlDirCheck = new RegExp("^[^" + ltrChars + "]*[" + rtlChars + "]");

//   return rtlDirCheck.test(s);
// }

tagColorOption.forEach((postTagColor, i) => {
  // create a list of bg and color for tag color options
  tagColorOptionsList.push([
    rgb2hex(tagColorOption[i].style.background),
    rgb2hex(tagColorOption[i].style.borderColor),
  ]);

  // default tag overview styling
  liveTagOverview.forEach((liveTag) => {
    liveTag.style.background = tagColorOptionsList[0][0];
    liveTag.style.color = tagColorOptionsList[0][1];
    liveTag.style.border = `3px solid ${tagColorOptionsList[0][1]}`;
    postTagColor.addEventListener("click", () => {
      liveTag.style.background = tagColorOptionsList[i][0];
      liveTag.style.color = tagColorOptionsList[i][1];
      liveTag.style.border = `3px solid ${tagColorOptionsList[i][1]}`;

      postTagPrimaryColorInput.value = tagColorOptionsList[i][0];
      postTagSecondaryColorInput.value = tagColorOptionsList[i][1];
      userTagPrimaryColorInput.value = tagColorOptionsList[i][0];
      userTagSecondaryColorInput.value = tagColorOptionsList[i][1];
    });
  });
});

postTagNameInput.addEventListener("keypress", function (e) {
  clearTimeout(timeout);
  timeout = setTimeout(function () {
    liveTagOverview[0].innerHTML = postTagNameInput.value;
  }, 1000);

  // setTimeout(function () {
  //   var isRTL = checkRTL(String.fromCharCode(e.charCode));
  //   var dir = isRTL ? "RTL" : "LTR";

  //   postTagNameInput.style.direction = dir;
  // }, 100);
});
userTagNameInput.addEventListener("keypress", function (e) {
  clearTimeout(timeout);
  timeout = setTimeout(function () {
    liveTagOverview[1].innerHTML = userTagNameInput.value;
  }, 1000);

  // setTimeout(function () {
  //   var isRTL = checkRTL(String.fromCharCode(e.charCode));
  //   var dir = isRTL ? "RTL" : "LTR";

  //   postTagNameInput.style.direction = dir;
  // }, 100);
});

const submitForm = (formName) => {
  form = document.getElementById(formName);
  form.submit();
};
