const btnThme = document.getElementById("btn-theme");

btnThme.addEventListener("click", () => changeTheme(btnThme));

/**
 * @param {HTMLElement} btnThme 
 */
function changeTheme(btnThme) {
  document.body.classList.toggle("bg-dark")
  document.body.classList.toggle("text-light")

  if (btnThme.innerText === "Light") {
    btnThme.innerText = "Dark"
  } else {
    btnThme.innerText = "Light"
  }
}