/**
 * @type {HTMLInputElement}
 */
const inputSymbol = document.getElementById("input-symbol");
const inputShares = document.getElementById("input-shares");
const buttonBuy = document.getElementById("button-buy");

function validateInputs() {
  if (inputSymbol.value && Number(inputShares.value) > 0) {
    buttonBuy.removeAttribute("disabled")
  } else {
    buttonBuy.setAttribute("disabled", "")
  }
}

inputSymbol.addEventListener("keyup", validateInputs)
inputShares.addEventListener("keyup", validateInputs)
inputShares.addEventListener("click", validateInputs)