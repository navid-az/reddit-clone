let postTypeBtn = document.querySelectorAll(".form-header button");
let fields = document.querySelectorAll(".field");
let postForm = document.getElementById("post-form");

// choose between post type options
function postType(i) {
  fields.forEach((field) => {
    field.style.display = "none";
  });
  postTypeBtn.forEach((btn) => {
    btn.style.background = "#3B3B3B";
  });
  fields[i].style.display = "block";
  postTypeBtn[i].style.background = "#FF3F18";
}
postType(0);
function submitBtn() {
  postForm.submit();
}

//server tab display
let serverSearchBar = document.getElementById("server-search-bar");
let serversTab = document.getElementById("servers-tab");
let is_closed = true;
let arrowIcon = document.getElementById("arrow-icon");

serverSearchBar.addEventListener("click", () => {
  if (is_closed == true) {
    serversTab.style.display = "flex";
    serverSearchBar.style.borderRadius = "0.5rem 0.5rem 0 0";
    is_closed = false;

    // server search bar arrow animation
    arrowIcon.style.transform = "rotate(90deg)";
  } else {
    serversTab.style.display = "none";
    serverSearchBar.style.borderRadius = "0.5rem";
    is_closed = true;
    arrowIcon.style.transform = "rotate(0deg)";
  }
});

//server names click
let server = document.querySelectorAll(".server");
let tag = document.querySelectorAll(".tag");
let serverImg = document.querySelectorAll(".server>img");
let serverField = document.getElementById("server-field");
let tagField = document.getElementById("tag-field");
let selectedServerImg = document.getElementById("selected-server-img");
let selectedServerName = document.getElementById("selected-server-name");

let serverTag = document.querySelectorAll(
  ".server>.server-info>p:nth-child(1)"
);
let serverTags = document.getElementById("server-tags");

const showServerTags = (serverTag) => {
  $.ajax({
    type: "GET",
    url: `/posts/create/${serverTag}/info`,
    success: function (response) {
      const data = response.data;
      if (data.length == 0) {
        serverTags.innerHTML = "";
      } else {
        serverTags.innerHTML = "";
        data.forEach((x) => {
          serverTags.innerHTML += `<div id='${x.id}' onclick='nigga(${x.id})' class="tag" style='background:${x.primary_color}; border:3.5px solid ${x.secondary_color}; color:${x.secondary_color}'>${x.name}</div> <br>`;
        });
      }
    },
    error: function (error) {
      console.log("error:", error);
    },
  });
};

const nigga = (Tag) => {
  console.log(Tag);
  tagField.value = Tag;
};

server.forEach((server, i) => {
  serverField.value = 1;
  server.addEventListener("click", () => {
    // server information request
    showServerTags(serverTag[i].innerHTML);

    // server search bar arrow animation
    arrowIcon.style.transform = "rotate(0deg)";

    selectedServerName.value = serverTag[i].innerHTML;
    selectedServerImg.src = serverImg[i].src;
    serverField.value = server.id;
    serversTab.style.display = "none";
    serverSearchBar.style.borderRadius = "0.5rem";
  });
});

showServerTags(selectedServerName.value);
