const limitationCreated = document.getElementById("creation-time").innerHTML;
const limitationDuration = document.getElementById("limit-duration").innerHTML;

if (limitationDuration == "permanent") {
  document.getElementById("limitTimer").innerHTML = "مجاز نیست";
} else {
  limitFor = parseInt(limitationDuration) * 24 * 60 * 60 * 1000;
  var count = setInterval(function () {
    const now = new Date().getTime();
    const creationTime = new Date(limitationCreated).getTime();
    const limitedUntil = creationTime + limitFor;
    const dateDiff = new Date(limitedUntil).getTime() - now;

    var days = Math.floor(dateDiff / (1000 * 60 * 60 * 24));
    var hours = Math.floor(
      (dateDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    );
    var minutes = Math.floor((dateDiff % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((dateDiff % (1000 * 60)) / 1000);

    document.getElementById("limitTimer").innerHTML = `${days}D ${
      hours < 10 ? "0" : ""
    }${hours}:${minutes < 10 ? "0" : ""}${minutes}:${
      seconds < 10 ? "0" : ""
    }${seconds}`;
  }, 1000);
}
