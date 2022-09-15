let searchInput = document.getElementById("search-input");
let searchResultTab = document.getElementById("search-result-tab");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
let link,
  resultName,
  resultType,
  alt = "";

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
      } else {
        if (searchInput.value.length > 0) {
          searchResultTab.style.display = "flex";
          searchResultTab.innerHTML = `
          <a >
          ${data}
          </a>`;
        } else {
          searchResultTab.style.display = "none";
        }
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
//  <a href='/r/${server.tag}' id='${server.id}' class='user'>
//               <img src="${server.image}" alt="">
//               <div class="server-info">
//                 <p>u/${server.tag}</p>
//                 <img src="/static/servers/svgs/plus.svg" alt="add moderator">
//               </div>
//             </a>
