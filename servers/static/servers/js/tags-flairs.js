let tagColorOption = document.querySelectorAll(".tag-color-option");
let tagColorOptionCheck = document.querySelectorAll(".tag-color-option > img");
//this code changes the above nodeList to array
// let tagColorOption = [...document.querySelectorAll(".tag-color-option")].slice(0,5);

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

// RGB code to HEX code
const rgb2hex = (rgb) =>
  `#${rgb
    .match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/)
    .slice(1)
    .map((n) => parseInt(n, 10).toString(16).padStart(2, "0"))
    .join("")}`;

for (let i = 0; i < tagColorOption.length; i++) {
  // create a list of bg and color for tag color options
  tagColorOptionsList.push([
    rgb2hex(tagColorOption[i].style.background),
    rgb2hex(tagColorOption[i].style.borderColor),
  ]);

  liveTagOverview.forEach((liveTag) => {
    // default tag overview styling
    liveTag.style.background = tagColorOptionsList[0][0];
    liveTag.style.color = tagColorOptionsList[0][1];
    liveTag.style.border = `3px solid ${tagColorOptionsList[0][1]}`;

    postTagPrimaryColorInput.value = tagColorOptionsList[0][0];
    postTagSecondaryColorInput.value = tagColorOptionsList[0][1];
    userTagPrimaryColorInput.value = tagColorOptionsList[0][0];
    userTagSecondaryColorInput.value = tagColorOptionsList[0][1];

    // tag overview styling
    tagColorOption[i].addEventListener("click", () => {
      liveTag.style.background = tagColorOptionsList[i][0];
      liveTag.style.color = tagColorOptionsList[i][1];
      liveTag.style.border = `3px solid ${tagColorOptionsList[i][1]}`;

      postTagPrimaryColorInput.value = tagColorOptionsList[i][0];
      postTagSecondaryColorInput.value = tagColorOptionsList[i][1];
      userTagPrimaryColorInput.value = tagColorOptionsList[i][0];
      userTagSecondaryColorInput.value = tagColorOptionsList[i][1];
    });
  });
}
// let form = document.getElementById("create-user-tag");
// if ((form.style.display = "none")) {
//   console.log("hello");
//   setDefaultColor();
// }

// typing tag name and updating live tag overview
postTagNameInput.addEventListener("keypress", function () {
  clearTimeout(timeout);
  timeout = setTimeout(function () {
    liveTagOverview[0].innerHTML = postTagNameInput.value;
  }, 1000);
});
userTagNameInput.addEventListener("keypress", function () {
  clearTimeout(timeout);
  timeout = setTimeout(function () {
    liveTagOverview[1].innerHTML = userTagNameInput.value;
  }, 1000);
});

// deleting tags animation
const deleteTag = (tagClass, deleteClass) => {
  let tagWrapper = document.querySelectorAll(`.${tagClass}`);
  let tagDeleteBtn = document.querySelectorAll(`.${deleteClass}`);

  tagWrapper.forEach((tag, index) => {
    if (tag.classList.contains("animate")) {
      tagDeleteBtn[index].style.display = "none";
      tag.classList.remove("animate");
    } else {
      tag.classList.add("animate");
      tagDeleteBtn.forEach((btn, index) => {
        btn.style.display = "flex";
        btn.addEventListener("mouseover", () => {
          btn.style.opacity = "1";
        });
        btn.addEventListener("mouseout", () => {
          btn.style.opacity = "0";
        });
      });
    }
  });
};

let pickTagColor = document.querySelectorAll(".pick-tag-color");
let pickTagColorLabel = document.querySelectorAll(
  ".pick-tag-color>section>label"
);
let pickTagColorInput = document.querySelectorAll(
  ".pick-tag-color>section>input"
);
let pickTagColorBtn = document.querySelectorAll(".pick-tag-color-btn");
let tabOpen = false;

const pickColorTab = (btnNum) => {
  if (tabOpen) {
    pickTagColor[btnNum].style.height = "0";
    console.log("height should change");
    pickTagColorLabel.forEach((label) => {
      label.style.opacity = "0";
    });
    tabOpen = false;
    console.log("its close", tabStatus);
  } else {
    pickTagColor[btnNum].style.height = "60px";
    pickTagColorLabel.forEach((label) => {
      label.style.opacity = "1";
    });
    pickTagColorInput.forEach((input) => {
      // change tag and live tag color with color inputs
      input.addEventListener("input", () => {
        if (btnNum == 0) {
          liveTagOverview[btnNum].style.background = pickTagColorInput[0].value;
          liveTagOverview[btnNum].style.color = pickTagColorInput[1].value;
          liveTagOverview[
            btnNum
          ].style.border = `3px solid ${pickTagColorInput[1].value}`;

          postTagPrimaryColorInput.value = pickTagColorInput[0].value;
          postTagSecondaryColorInput.value = pickTagColorInput[1].value;
        } else {
          liveTagOverview[btnNum].style.background = pickTagColorInput[2].value;
          liveTagOverview[btnNum].style.color = pickTagColorInput[3].value;
          liveTagOverview[
            btnNum
          ].style.border = `3px solid ${pickTagColorInput[3].value}`;
          userTagPrimaryColorInput.value = pickTagColorInput[2].value;
          userTagSecondaryColorInput.value = pickTagColorInput[3].value;
        }
      });
    });

    tabOpen = true;
    console.log("its open", tabStatus);
  }
  return btnNum;
};

// if (createServerTabFunc()) {
//   pickTagColor[btnNum].style.height = "0";
//   pickTagColorLabel.forEach((label) => {
//     label.style.opacity = "0";
//   });
//   tabOpen = false;
// }

const submitForm = (formName) => {
  form = document.getElementById(formName);
  form.submit();
};
