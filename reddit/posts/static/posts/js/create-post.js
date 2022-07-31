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
let serverDetailsWrapper = document.getElementById("server-details-wrapper");

const showServerTags = (serverTag) => {
  $.ajax({
    type: "GET",
    url: `/posts/create/${serverTag}/info`,
    success: function (response) {
      const tagData = response.data.slice(1);
      const serverData = response.data.shift();
      if (tagData.length == 0) {
        serverTags.innerHTML = "";
      } else {
        serverTags.innerHTML = "";
        tagData.forEach((x) => {
          serverTags.innerHTML += `<div id='${x.id}' onclick='nigga(${x.id})' class="tag" style='background:${x.primary_color}; border:3.5px solid ${x.secondary_color}; color:${x.secondary_color}'>${x.name}</div> <br>`;
        });
      }
      ali = serverData[0].fields;
      console.log(ali.about);
      // server information
      serverDetailsWrapper.innerHTML = `
        <div class="server-details">
        <div class="server-details-header">
          <img
            class="server-header-img"
            src="/media/${ali.header_image}"
            alt="server header image"
          />
          <img
            class="server-img"
            src="/media/${ali.image}"
            alt="server header image"
          />
          <div class="server-tag">r/${ali.tag}</div>
        </div>
        <div class="server-details-info">
          <div class="about-server">
            <h3>درباره این سرور</h3>
            <p>${ali.about}</p>
          </div>
          <div class="server-numbers-wrapper">
            <div class="server-numbers">
              <div class="followers">
                <p>${ali.followers}</p>
                <p>دنبال کننده</p>
              </div>
              <div class="online_users">
                <p>0</p>
                <p>آنلاین</p>
              </div>
            </div>
            <div class="server-score">
              <h2>#۸۷</h2>
            </div>
          </div>
          <div class="server-created-at">
            <span>
              <img src="{% static 'servers/svgs/gift.svg' %}" alt="" />
              <h3>ساخته شده در تاریخ</h3>
            </span>
            <p>${ali.created.slice(0, 10)}</p>
          </div>
        </div>
      </div>
        `;
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
