let rangeSliderSectionIndicators = document.querySelectorAll(
  ".range-slider-section-indicator"
);
let rangeSliderSectionIndicatorDivs = document.querySelectorAll(
  ".range-slider-section-indicator > div"
);
let rangeSliderSectionIndicatorNums = document.querySelectorAll(
  ".range-slider-section-indicator > p"
);
let rangeSliderSectionLines = document.querySelectorAll(
  ".range-slider-section-line"
);
let rangeSliderBtn = document.getElementById("range-slider-btn");
let durationInput = document.getElementById("id_duration");
let userInput = document.getElementById("id_user");
let defaultPosition = 79;

const changeColor = (indicatorNum) => {
  for (var i = 0; i <= 5; i++) {
    rangeSliderSectionIndicatorDivs[i].style.background = "#D9D9D9";
    rangeSliderSectionIndicatorNums[i].style.color = "#D9D9D9";
  }
  for (var i = 0; i <= 4; i++) {
    rangeSliderSectionLines[i].style.background = "#D9D9D9";
  }
  for (var i = 0; i <= indicatorNum; i++) {
    rangeSliderSectionIndicatorDivs[i].style.background = "#FF3F18";
    rangeSliderSectionIndicatorNums[i].style.color = "#FF3F18";
  }
  for (var i = 0; i <= indicatorNum - 1; i++) {
    rangeSliderSectionLines[i].style.background = "#FF3F18";
  }
};

const changeDuration = (indicatorNum) => {
  if (indicatorNum == 0) {
    rangeSliderBtn.style.left = "0px";
    durationInput.value = 1;
    changeColor(indicatorNum);
  } else if (indicatorNum == 1) {
    rangeSliderBtn.style.left = `${defaultPosition}px`;
    durationInput.value = 2;
    changeColor(indicatorNum);
  } else if (indicatorNum == 2) {
    rangeSliderBtn.style.left = `${defaultPosition * 2}px`;
    durationInput.value = 7;
    changeColor(indicatorNum);
  } else if (indicatorNum == 3) {
    rangeSliderBtn.style.left = `${defaultPosition * 3}px`;
    durationInput.value = 14;
    changeColor(indicatorNum);
  } else if (indicatorNum == 4) {
    rangeSliderBtn.style.left = `${defaultPosition * 4}px`;
    durationInput.value = 30;
    changeColor(indicatorNum);
  } else if (indicatorNum == 5) {
    rangeSliderBtn.style.left = `${defaultPosition * 5}px`;
    durationInput.value = "permanent";
    changeColor(indicatorNum);
  }
};

rangeSliderSectionIndicators.forEach((indic, index) => {
  rangeSliderSectionIndicators[index].addEventListener(
    "click",
    changeDuration.bind(null, index)
  );
});

let listItems = document.querySelectorAll(".list-item");

const changeReportedUser = (userId) => {
  userInput.value = userId;
};

let deleteReportBtn = document.querySelectorAll(".delete-report-btn");
let deleteReportIcon = document.querySelectorAll(
  ".list-item-title>a>img[alt='delete report']"
);
let ReportIcon = document.querySelectorAll(
  ".list-item-title>a>img[alt='report icon']"
);

deleteReportBtn.forEach((btn) => {
  btn.addEventListener("mouseover", (e) => {
    imgId = e.target.id;
    deleteReportIcon[imgId].style.display = "flex";
    ReportIcon[imgId].style.display = "none";
  });
  btn.addEventListener("mouseout", (e) => {
    imgId = e.target.id;
    deleteReportIcon[imgId].style.display = "none";
    ReportIcon[imgId].style.display = "flex";
  });
});
