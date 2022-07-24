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
let serverField = document.getElementById("server-field");
let selectedServerImg = document.getElementById("selected-server-img");
let selectedServerName = document.getElementById("selected-server-name");

server.forEach((server, i) => {
  serverField.value = 1;
  let serverTag = document.querySelectorAll(
    ".server>.server-info>p:nth-child(1)"
  );
  let serverImg = document.querySelectorAll(".server>img");

  server.addEventListener("click", () => {
    arrowIcon.style.transform = "rotate(0deg)";
    selectedServerName.value = serverTag[i].innerHTML;
    // console.log(serverImg[i].src);
    selectedServerImg.src = serverImg[i].src;
    // console.log(serverTag[i].innerHTML);
    serverField.value = server.id;
    // console.log(serverField.value);
    serversTab.style.display = "none";
    serverSearchBar.style.borderRadius = "0.5rem";
  });
});
