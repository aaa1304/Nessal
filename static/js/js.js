
let toggler = document.getElementById("toggler");
let close_icon = document.getElementById("close-icon");
let body = document.getElementById("body")
 

let sidebar = document.querySelector(".sidebar");
let opacity = document.querySelector(".opacity");


toggler.onclick = function(){
  sidebar.style.display = "block";
  opacity.style.display = "block";
};
close_icon.onclick = function(){
  sidebar.style.display = "none";
  opacity.style.display = "none";
};


// let btn_show_categoty = document.getElementById("btn-show-categoty");
// let btn_close_categoty = document.getElementById("btn-close-categoty");

// let parent_category = document.getElementById("parent-category");

// btn_show_categoty.onclick = function(){
//   parent_category.style.display = "block";
//   btn_show_categoty.style.display = "none";
// };

// btn_close_categoty.onclick = function(){
//   parent_category.style.display = "none";
//   btn_show_categoty.style.display = "flex";

// };

// nav
let not_work = document.getElementById("not-work");
let not_workb = document.getElementById("not-workb");

not_work.onclick = function(){
  div_alert.style.display = "flex";
};

not_workb.onclick = function(){
  div_alert.style.display = "flex";
};

// sidebar
let not_works = document.getElementById("not-works");
let not_workl = document.getElementById("not-workl");

not_works.onclick = function(){
  div_alert.style.display = "flex";
  div_alert.style.zIndex = "1000000000000";

};

not_workl.onclick = function(){
  div_alert.style.display = "flex";
  div_alert.style.zIndex = "1000000000000";

};

// alert
let div_alert = document.getElementById("div-alert");

let icon_close = document.getElementById("icon-close");

icon_close.onclick = function() {
  div_alert.style.display = "none";

};







