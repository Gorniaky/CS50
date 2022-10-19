/**
 * @type {HTMLSelectElement}
 */
const inputSymbol = document.getElementById("input-symbol");
const inputShares = document.getElementById("input-shares");
const buttonSell = document.getElementById("button-sell");

function validateInputs() {
  if (inputSymbol.value && Number(inputShares.value) > 0) {
    buttonSell.removeAttribute("disabled")
  } else {
    buttonSell.setAttribute("disabled", "")
  }
}

inputShares.addEventListener("keyup", validateInputs)
inputSymbol.addEventListener("click", validateInputs)
inputShares.addEventListener("click", validateInputs)