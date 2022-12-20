let ruleDetailBtn = document.querySelectorAll(".rule-detail-btn");
let listItemBody = document.querySelectorAll(".list-item-body");
let displayStatus = false;

const openRuleDetails = (ruleNum) => {
  if (displayStatus == true) {
    listItemBody[ruleNum].style.display = "none";
    displayStatus = false;
    console.log(displayStatus);

    console.log("close");
  } else {
    listItemBody.forEach((i) => {
      i.style.display = "none";
      console.log("close others");
    });
    listItemBody[ruleNum].style.display = "flex";
    console.log("open this");
    displayStatus = true;
    console.log(displayStatus);
  }
};
// ruleDetailBtn.forEach((detailBtn, i) => {
//   detailBtn[i].addEventListener("click", openRuleDetails);
// });
