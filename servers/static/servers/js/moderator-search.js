const moderatorSearchInput = document.getElementById("moderator-search-input");
const searchResultsTab = document.getElementById("search-results-tab");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const sendData = (username) => {
  $.ajax({
    type: "POST",
    url: "/r/get-moderator/",
    data: {
      csrfmiddlewaretoken: csrf,
      user: username,
    },
    success: (response) => {
      const data = response.data;
      console.log(data);
      if (Array.isArray(data)) {
        searchResultsTab.innerHTML = "";
        data.forEach((user) => {
          searchResultsTab.innerHTML += `${user.username} <img src="${user.image}"> <br>`;
        });
      } else {
        if (moderatorSearchInput.value.length > 0) {
          searchResultsTab.innerHTML = `${data}`;
        } else {
          searchResultsTab.classList.add = "d-none";
        }
      }
    },
    error: (err) => {
      console.log(err);
    },
  });
};

moderatorSearchInput.addEventListener("keyup", (e) => {
  sendData(e.target.value);
});
