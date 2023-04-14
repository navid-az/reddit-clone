let tabStatus = true;

// form tab open and close function
const createServerTabFunc = (formId, var1) => {
  let form = document.getElementById(formId);

  if (tabStatus == true) {
    form.style.display = "flex";
    setTimeout(() => {
      form.style.opacity = "1";
    }, 100);
    tabStatus = false;
  } else {
    form.style.opacity = "0";
    setTimeout(() => {
      form.style.display = "none";
    }, 500);
    tabStatus = true;
  }
};

UserlocationIndicator = document.getElementById("user-indicator");
ServerlocationIndicator = document.getElementById("server-indicator");

if (window.location.href.includes("/r/")) {
  ServerlocationIndicator.style.display = "flex";
} else if (window.location.href.includes("/u/")) {
  UserlocationIndicator.style.display = "flex";
}
