/**
 * @type {HTMLInputElement}
 */
const inputSymbol = document.getElementById("input-symbol");
const buttonQuote = document.getElementById("button-quote");

inputSymbol.addEventListener("keyup", function() {
  if (inputSymbol.value) {
    buttonQuote.removeAttribute("disabled")
  } else {
    buttonQuote.setAttribute("disabled", "")
  }
})