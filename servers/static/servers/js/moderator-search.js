const moderatorSearchInput = document.getElementById("moderator-search-input");
const searchResultsTab = document.getElementById("search-results-tab");
const csrff = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const input = document.getElementById("id_user");
const moderatorSearchWrapper = document.getElementById(
  "moderator-search-wrapper"
);

const sendData = (username) => {
  $.ajax({
    type: "POST",
    url: "/r/get-moderators/",
    data: {
      csrfmiddlewaretoken: csrff,
      user: username,
    },
    success: (response) => {
      const data = response.data;
      console.log(data);
      if (Array.isArray(data)) {
        searchResultsTab.innerHTML = "";
        data.forEach((user) => {
          searchResultsTab.innerHTML += `
            <div id='${user.id}' class='user'>
              <img src="${user.image}" alt="">
              <div class="server-info">
                <p>u/${user.username}</p>
                <img onclick='addModerator(${user.id})' src="/static/servers/svgs/plus.svg" alt="add moderator">
              </div>
            </div> 
          `;
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

const addModerator = (id) => {
  input.value = id;
  moderatorSearchWrapper.submit();
};
