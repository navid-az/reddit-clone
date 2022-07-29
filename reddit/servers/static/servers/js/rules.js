let ruleDetailBtn = document.querySelectorAll(".rule-detail-btn");
let ruleBody = document.querySelectorAll(".rule-body");
let displayStatus = false;

const openRuleDetails = (ruleNum) => {
  if (displayStatus == true) {
    ruleBody[ruleNum].style.display = "none";
    displayStatus = false;
    console.log(displayStatus);

    console.log("close");
  } else {
    ruleBody.forEach((i) => {
      i.style.display = "none";
      console.log("close others");
    });
    ruleBody[ruleNum].style.display = "flex";
    console.log("open this");
    displayStatus = true;
    console.log(displayStatus);
  }
};
// ruleDetailBtn.forEach((detailBtn, i) => {
//   detailBtn[i].addEventListener("click", openRuleDetails);
// });
