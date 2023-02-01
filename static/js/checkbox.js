let checkboxBtn = document.querySelectorAll(".checkbox-btn");
let checkboxInputs = document.querySelectorAll("input[type=checkbox]");
const formSubmitBtn = document.getElementById("s-submit-btn");

checkboxInputs.forEach((input, index) => {
  if (checkboxInputs[index].checked) {
    checkboxBtn[index].style.background = "#FF3F18";
    checkboxBtn[index].style.border = "none";
  } else {
    checkboxBtn[index].style.background = "none";
    checkboxBtn[index].style.border = "3px solid rgba(0, 0, 0, 0.09)";
  }
});

const checkboxForm = (checkboxId) => {
  formSubmitBtn.style.background = "#FF3F18";
  formSubmitBtn.style.color = "#FFFF";
  formSubmitBtn.style.cursor = "pointer";
  formSubmitBtn.style.pointerEvents = "auto";

  var a = event.target.parentElement;
  const checkbox = document.getElementById(checkboxId);
  if (checkbox.checked) {
    a.style.background = "none";
    a.style.border = "3px solid rgba(0, 0, 0, 0.09)";
    checkbox.checked = false;
  } else {
    a.style.background = "#FF3F18";
    a.style.border = "none";
    checkbox.checked = true;
  }
};
