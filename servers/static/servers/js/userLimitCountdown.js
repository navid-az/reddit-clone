const limitationCreated = document.getElementById("creation-time").innerHTML;
const limitationDuration =
  parseInt(document.getElementById("limit-duration").innerHTML) *
  24 *
  60 *
  60 *
  1000;

var count = setInterval(function () {
  const now = new Date().getTime();
  const creationTime = new Date(limitationCreated).getTime();
  const limitedUntil = creationTime + limitationDuration;
  const dateDiff = new Date(limitedUntil).getTime() - now;
  console.log(new Date(), "/n", new Date(limitationCreated));
  var days = Math.floor(dateDiff / (1000 * 60 * 60 * 24));
  var hours = Math.floor((dateDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((dateDiff % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((dateDiff % (1000 * 60)) / 1000);

  document.getElementById("limitTimer").innerHTML = `${days}D ${
    hours < 10 ? "0" : ""
  }${hours}:${minutes < 10 ? "0" : ""}${minutes}:${
    seconds < 10 ? "0" : ""
  }${seconds}`;
}, 1000);
