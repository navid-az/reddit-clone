let searchInput = document.getElementById("search-input");
let searchResultTab = document.getElementById("search-result-tab");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
let link,
  resultName,
  resultType,
  alt = "";

// search btns
let deleteSearchBtn = document.getElementById("delete-search");
let searchBtn = document.getElementById("search-btn");

const deleteSearch = (e) => {
  e.preventDefault();
  searchInput.value = "";
  searchResultTab.style.display = "none";
  deleteSearchBtn.style.opacity = 0;
  searchBtn.style.opacity = 1;
  setTimeout(() => {
    searchBtn.style.display = "flex";
    deleteSearchBtn.style.display = "none";
  }, 250);
};
const startSearch = (e) => {
  e.preventDefault();
  searchInput.focus();
  deleteSearchBtn.style.display = "flex";
  setTimeout(() => {
    deleteSearchBtn.style.opacity = 1;
    searchBtn.style.display = "none";
    searchBtn.style.opacity = 0;
  }, 250);
};
deleteSearchBtn.addEventListener("click", deleteSearch);
searchBtn.addEventListener("click", startSearch);
//

const searched = (word) => {
  $.ajax({
    type: "POST",
    url: "/search/",
    data: {
      csrfmiddlewaretoken: csrf,
      searchedWord: word,
    },
    success: (response) => {
      const data = response.data;

      // search btn & delete search btn animation
      deleteSearchBtn.style.display = "flex";
      setTimeout(() => {
        deleteSearchBtn.style.opacity = 1;
        searchBtn.style.display = "none";
        searchBtn.style.opacity = 0;
      }, 250);
      //

      if (Array.isArray(data)) {
        searchResultTab.style.display = "flex";
        searchResultTab.innerHTML = "";
        data.forEach((result) => {
          if (result.tag) {
            link = `http://127.0.0.1:8000/r/${result.tag}`;
            alt = "server image";
            resultType = "r";
            resultName = result.tag;
          } else {
            link = `http://127.0.0.1:8000/u/${result.username}/profile`;
            alt = "user image";
            resultType = "u";
            resultName = result.username;
          }
          searchResultTab.innerHTML += `
            <a href='${link}' id='${result.id}' class='search-result'>
              <img src="${result.image}" alt="${alt}">
              <div class="result-info">
                <p>${resultType}/${resultName}</p>
                <p>عضو ${result.followers_count}</p>
              </div>
            </a> 
          `;
        });

        // while the data doesn't exist
      } else {
        if (searchInput.value.length > 0) {
          searchResultTab.style.display = "flex";
          searchResultTab.innerHTML = `
          <div id="no-result-tab">
            <img src="/static/svgs/sad-reddit-logo.svg">
            <p>موردی یافت نشد</p>
          </div>`;
        } else {
          searchResultTab.style.display = "none";
        }
      }

      // close the result tab if empty
      if (searchInput.value.length == 0) {
        searchResultTab.style.display = "none";
        deleteSearchBtn.style.opacity = 0;
      }
    },
    error: (err) => {
      searchResultTab.style.display = "none";
      console.log(err);
    },
  });
};
searchInput.addEventListener("keyup", (e) => {
  searched(e.target.value);
});
