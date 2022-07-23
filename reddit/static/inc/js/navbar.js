let tabStatus = true;
let createServerTab = document.getElementById("create-server-tab");
let grayLayer = document.getElementById("gray-layer");

// create server tab open and close function
const createServerTabFunc = () => {
  if (tabStatus == true) {
    grayLayer.style.display = "flex";
    setTimeout(() => {
      grayLayer.style.opacity = "1";
    }, 100);
    tabStatus = false;
  } else {
    grayLayer.style.opacity = "0";
    setTimeout(() => {
      grayLayer.style.display = "none";
    }, 500);
    tabStatus = true;
  }
};
