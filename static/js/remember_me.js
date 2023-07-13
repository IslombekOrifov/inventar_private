const rmCheck = document.getElementById("rememberMe"),
    userInput = document.getElementById("id_username");
    passInput = document.getElementById("id_password");

if (localStorage.checkbox && localStorage.checkbox !== "") {
  rmCheck.setAttribute("checked", "checked");
  userInput.value = localStorage.username;
  passInput.value = localStorage.password;
} else {
  rmCheck.removeAttribute("checked");
  userInput.value = "";
  passInput.value = "";
}

function lsRememberMe() {
  if (rmCheck.checked && userInput.value !== "") {
    localStorage.username = userInput.value;
    localStorage.password = passInput.value;
    localStorage.checkbox = rmCheck.value;
  } else {
    localStorage.username = "";
    localStorage.password = "";
    localStorage.checkbox = "";
  }
}



function detailSendPage(e) {
  a = e.getAttribute("data-href");
  console.log(a);
  window.location.href = a;
}