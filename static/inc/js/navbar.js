let tabStatus = true;

// form tab open and close function
const createServerTabFunc = (formId, var1) => {
  let form = document.getElementById(formId);
  console.log(form);

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
