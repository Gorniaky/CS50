/**
 * @type {HTMLInputElement}
 */
const inputUsername = document.getElementById("input-username");
/**
 * @type {HTMLInputElement}
 */
const inputPassword = document.getElementById("input-password");
const buttonLogin = document.getElementById("button-login");

function inputVerify() {
  if (inputUsername.value && inputPassword.value) {
    buttonLogin.removeAttribute("disabled")
  } else {
    buttonLogin.setAttribute("disabled", "")
  }
}

inputUsername.addEventListener("keyup", inputVerify)
inputPassword.addEventListener("keyup", inputVerify)