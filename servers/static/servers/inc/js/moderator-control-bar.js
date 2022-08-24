let serverList = document.getElementById("server-list");
let is_open = false;

$.ajax({
  type: "GET",
  url: "/r/moderating-page/",
  success: function (response) {
    let data = response.data;
    if (data.length > 3) {
      serverList.style.overflowY = "scroll";
      serverList.style.overflowX = "hidden";
      serverList.style.height = "9.9rem";
    } else {
      serverList.style.height = "auto";
    }
    data.forEach((x) => {
      if (x.server_type == "pri") {
        serverList.innerHTML += `
        <a class='server-list-options' href='http://127.0.0.1:8000/r/${x.tag}/moderating-page/' class='choose-server-list-options'>
          <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 13H2" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M5.45 5.61L2 12.5V18.5C2 19.0304 2.21071 19.5391 2.58579 19.9142C2.96086 20.2893 3.46957 20.5 4 20.5H20C20.5304 20.5 21.0391 20.2893 21.4142 19.9142C21.7893 19.5391 22 19.0304 22 18.5V12.5L18.55 5.61C18.3844 5.27679 18.1292 4.99637 17.813 4.80028C17.4967 4.60419 17.1321 4.5002 16.76 4.5H7.24C6.86792 4.5002 6.50326 4.60419 6.18704 4.80028C5.87083 4.99637 5.61558 5.27679 5.45 5.61Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M6 16.5H6.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M10 16.5H10.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M21.2917 16.9584H13.7083C13.11 16.9584 12.625 17.4434 12.625 18.0417V21.8334C12.625 22.4317 13.11 22.9167 13.7083 22.9167H21.2917C21.89 22.9167 22.375 22.4317 22.375 21.8334V18.0417C22.375 17.4434 21.89 16.9584 21.2917 16.9584Z" fill="#FF3F18" stroke="#FF3F18" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M14.792 16.9584V14.7917C14.792 14.0734 15.0773 13.3845 15.5852 12.8766C16.0932 12.3687 16.782 12.0834 17.5003 12.0834C18.2186 12.0834 18.9075 12.3687 19.4154 12.8766C19.9233 13.3845 20.2087 14.0734 20.2087 14.7917V16.9584" stroke="#FF3F18" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <p>r/${x.tag}</p>
        </a>
        `;
      } else {
        serverList.innerHTML += `
        <a class='server-list-options' href='http://127.0.0.1:8000/r/${x.tag}/moderating-page/' class='choose-server-list-options'>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 12H2" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M5.45 5.11L2 12V18C2 18.5304 2.21071 19.0391 2.58579 19.4142C2.96086 19.7893 3.46957 20 4 20H20C20.5304 20 21.0391 19.7893 21.4142 19.4142C21.7893 19.0391 22 18.5304 22 18V12L18.55 5.11C18.3844 4.77679 18.1292 4.49637 17.813 4.30028C17.4967 4.10419 17.1321 4.0002 16.76 4H7.24C6.86792 4.0002 6.50326 4.10419 6.18704 4.30028C5.87083 4.49637 5.61558 4.77679 5.45 5.11V5.11Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M6 16H6.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M10 16H10.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <p>r/${x.tag}</p>
        </a>
      `;
      }
    });
    return data;
  },
  error: function (error) {
    console.log(error);
  },
});

const openChooseServerList = () => {
  if (is_open) {
    serverList.style.display = "none";
    is_open = false;
  } else {
    serverList.style.display = "flex";
    serverList.style.borderRadius = "0 0 0.5rem 0.5rem";
    is_open = true;
  }
};
