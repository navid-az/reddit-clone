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
  fields[i].style.display = "flex";
  postTypeBtn[i].style.background = "#FF3F18";
}

// default post type
postType(0);
function submitBtn() {
  postForm.submit();
}

//server tab display
let serverSearchBar = document.getElementById("server-search-bar");
let serversTab = document.getElementById("servers-tab");
let arrowIcon = document.getElementById("arrow-icon");
let is_closed = true;

// server search bar arrow animation
serverSearchBar.addEventListener("click", () => {
  if (is_closed == true) {
    serversTab.style.display = "flex";
    serverSearchBar.style.borderRadius = "0.5rem 0.5rem 0 0";
    is_closed = false;

    arrowIcon.style.transform = "rotate(90deg)";
  } else {
    serversTab.style.display = "none";
    serverSearchBar.style.borderRadius = "0.5rem";
    is_closed = true;
    arrowIcon.style.transform = "rotate(0deg)";
  }
});

//server names click

// hidden inputs
let serverField = document.getElementById("server-field");
let tagField = document.getElementById("tag-field");

let tags = document.querySelectorAll(".tags");
let server = document.querySelectorAll(".server");
let serverImg = document.querySelectorAll(".server>img");

let selectedServerName = document.getElementById("selected-server-name");
let selectedServerImg = document.getElementById("selected-server-img");

let serverTag = document.querySelectorAll(
  ".server>.server-info>p:nth-child(1)"
);
let serverTags = document.getElementById("server-tags");
let serverDetails = document.getElementById("server-details");
let rulesWrapper = document.getElementById("rules-wrapper");

const showData = (serverTag) => {
  $.ajax({
    type: "GET",
    url: `/posts/create/${serverTag}/info`,
    success: function (response) {
      const ruleData = [];
      const tagData = [];
      const serverData = response.data.shift();

      // checking for tags and rules and separating them
      for (let i = 0; i < response.data.length; i++) {
        const object = response.data[i];
        if ("title" in object) {
          ruleData.push(object);
        } else {
          tagData.push(object);
        }
      }

      // inserting tags into DOM
      if (tagData.length == 0) {
        serverTags.innerHTML = "";
      } else {
        serverTags.innerHTML = "";
        tagData.forEach((x) => {
          serverTags.innerHTML += `<div id='${x.id}' onclick='choosePostTag(${x.id})' class="tags" style='background:${x.primary_color}; border:3.5px solid ${x.secondary_color}; color:${x.secondary_color}'>${x.name}</div> <br>`;
        });
      }

      var server = serverData[0].fields;
      // server information
      serverDetails.innerHTML = `
        <div class="server-details-header">
          <img
            class="server-header-img"
            src="/media/${server.header_image}"
            alt="server header image"
          />
          <img
            class="server-img"
            src="/media/${server.image}"
            alt="server header image"
          />
          <div class="server-tag">r/${server.tag}</div>
        </div>
          <section>
            <h3>درباره این سرور</h3>
            <p>${server.about}</p>
          </section>
          <div class="server-numbers-wrapper">
            <div class="server-numbers">
              <div class="followers">
                <p>${server.followers}</p>
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
          <section>
            <span>
              <img src="{% static 'servers/svgs/gift.svg' %}" alt="" />
              <h3>ساخته شده در تاریخ</h3>
            </span>
            <p>${server.created.slice(0, 10)}</p>
          </section>
        `;

      // rules information
      rulesWrapper.innerHTML = "";
      ruleData.forEach((rule, i) => {
        rulesWrapper.innerHTML += `
        <div class='rule'>
          <div id='rule-title' class='rule-title' onclick='showRuleDetail(${
            i + 1
          })'>
            <div>
              <p>${i + 1}.</p>
              <p>${rule.title}</p>
            </div>
            <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.5 5.5L7.5 10.5L12.5 15.5" stroke="#1E1E20" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class='rule-body'>
            <p>${rule.body}</p>
          </div>
        </div>
      `;
      });
    },
    error: function (error) {
      console.log("error:", error);
    },
  });
};

let ruleBody = document.querySelectorAll(".rule-body");

const choosePostTag = (Tag) => {
  selectedTag = document.getElementById(Tag);
  // selectedTag.style.background = "red";
  tagField.value = Tag;
};

server.forEach((server, i) => {
  serverField.value = 1;
  server.addEventListener("click", () => {
    // server information request
    showData(serverTag[i].innerHTML);

    // server search bar arrow animation
    arrowIcon.style.transform = "rotate(0deg)";

    selectedServerName.value = serverTag[i].innerHTML;
    selectedServerImg.src = serverImg[i].src;
    serverField.value = server.id;
    serversTab.style.display = "none";
    serverSearchBar.style.borderRadius = "0.5rem";
  });
});

showData(selectedServerName.value);

// uploading image and video
let dropZones = document.querySelectorAll(".upload-file-field > input");
let dropZone = document.querySelectorAll(".upload-file-field");
let uploadIcons = document.querySelectorAll(".upload-icon");
let defaultIcons = document.querySelectorAll(".default-icon");
let uploadedFilesWrapper = document.querySelectorAll(".uploaded-files-wrapper");

const hello = (fileType) => {
  uploadIcons.forEach((ui) => {
    ui.style.display = "flex";
  });
  defaultIcons.forEach((di) => {
    di.style.display = "none";
  });
  dropZone[fileType].classList.add("drag-over");
};
const bye = (fileType) => {
  uploadIcons.forEach((ui) => {
    ui.style.display = "none";
  });
  defaultIcons.forEach((di) => {
    di.style.display = "flex";
  });
  dropZone[fileType].classList.remove("drag-over");
};

let deleteBtn = `<svg width="31" height="31" viewBox="0 0 31 31" fill="currentcolor" xmlns="http://www.w3.org/2000/svg">
<path d="M23.25 7.75L7.75 23.25" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7.75 7.75L23.25 23.25" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`;

dropZones.forEach((dz, index) => {
  dz.addEventListener("dragover", () => {
    hello(index);
  });
  dz.addEventListener("dragleave", () => {
    bye(index);
  });

  dz.addEventListener("change", (e) => {
    const uploadedFilesField = document.querySelector(
      ".upload-file-field >input"
    );
    if (e.target.id == "id_image") {
      const reader = new FileReader();
      reader.addEventListener("load", () => {
        uploadedFilesWrapper[0].innerHTML = `<div class="uploaded-files"><div class="delete-file-btn" onclick="deleteFile()">${deleteBtn}</div> <img src="${reader.result}"></img></div>`;
        uploadedFilesWrapper[0].style.zIndex = "0";
      });
      reader.readAsDataURL(uploadedFilesField.files[0]);
    } else {
      const reader = new FileReader();
      reader.addEventListener("load", () => {
        uploadedFilesWrapper[1].innerHTML = `<div class="uploaded-files"><div onclick="deleteFile()">delete</div> <img src="${reader.result}"></img></div>`;
        uploadedFilesWrapper[1].style.zIndex = "0";
      });
      reader.readAsDataURL(uploadedFilesField.files[0]);
    }
  });
});
imageInput = document.getElementById("id_image");
const deleteFile = (e) => {
  imageInput.value = "";
  dropZone.forEach((dz) => {
    dz.classList.remove("drag-over");
  });
  uploadedFilesWrapper[0].style.zIndex = "-1";
};
