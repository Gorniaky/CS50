/**
 * @type {HTMLInputElement}
 */
const inputUsername = document.getElementById("input-username");
/**
 * @type {HTMLInputElement}
 */
const inputPassword = document.getElementById("input-password");
/**
 * @type {HTMLInputElement}
 */
const inputVerifyPassword = document.getElementById("input-verify-password");
const buttonRegister = document.getElementById("button-register");
const divUsername = document.getElementById("div-username");
const divVerifyPassword = document.getElementById("div-verify-password");

const pUsernameMissing = document.createElement("p")
pUsernameMissing.innerText = "Username already exists!"

const pPasswordNotEqual = document.createElement("p")
pPasswordNotEqual.innerText = "Both passwords must be the same!"

let userExists = false

async function formUsernameVerify() {
  if (!inputUsername.value) {
    buttonRegister.setAttribute("disabled", "")
    return
  }

  /**
   * @type {Record<"user", boolean>}
   */
  const json = await fetch("/user?username=" + inputUsername.value).then(r => r.json())

  userExists = json.user

  if (userExists) {
    buttonRegister.setAttribute("disabled", "")

    if (divUsername.children.length === 1)
      divUsername.appendChild(pUsernameMissing)
  } else {
    if (divUsername.children.length === 2)
      divUsername.removeChild(pUsernameMissing)

    formPasswordVerify()
  }
}

function formPasswordVerify() {
  if (formVerifyPasswordVerify() || !inputPassword.value || userExists) {
    buttonRegister.setAttribute("disabled", "")
    return
  }

  buttonRegister.removeAttribute("disabled")
}

function formVerifyPasswordVerify() {
  if (inputPassword.value === inputVerifyPassword.value) {
    if (divVerifyPassword.children.length === 2)
      divVerifyPassword.removeChild(pPasswordNotEqual)

    return false
  } else {
    if (divVerifyPassword.children.length === 1)
      divVerifyPassword.appendChild(pPasswordNotEqual)

    return true
  }
}

inputUsername.addEventListener("keyup", formUsernameVerify)
inputPassword.addEventListener("keyup", formPasswordVerify)
inputVerifyPassword.addEventListener("keyup", formPasswordVerify)