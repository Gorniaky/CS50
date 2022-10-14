import trivia from "./trivia.json" assert { type: "json" };
trivia.multiple = trivia.results
trivia.free = trivia.results
const secMultiple = document.querySelector("#multiple");
const secFree = document.querySelector("#free");

/**
 * @type {QuestData}
 */
let mQuest;

/**
 * @type {QuestData}
 */
let fQuest;

function initMultipleTrivia() {
  mQuest = trivia.multiple.splice(Math.floor(Math.random() * trivia.multiple.length), 1)[0];

  const header = document.createElement("h3");
  header.textContent = mQuest.question;

  const alert = document.createElement("h4");

  const answers_buttons = document.createElement("div");

  const answers = [mQuest.correct_answer].concat(mQuest.incorrect_answers).sort(() => Math.random() - 0.5);
  for (let i = 0; i < answers.length; i++) {
    const answer = answers[i];

    const btn = document.createElement("button");
    btn.textContent = answer;

    answers_buttons.appendChild(btn);

    btn.addEventListener("click", () => {
      if (btn.textContent === mQuest.correct_answer) {
        btn.classList.add("bg-green");
        alert.textContent = "Correct!";
      } else {
        btn.classList.add("bg-red");
        alert.textContent = "Incorrect!";
      }
    })
  }

  secMultiple.append(header, alert, answers_buttons);
}

function initFreeTrivia() {
  fQuest = trivia.free.splice(Math.floor(Math.random() * trivia.free.length), 1)[0];

  const header = document.createElement("h3");
  header.textContent = fQuest.question;

  const alert = document.createElement("h4");

  const input = document.createElement("input");
  input.type = "text"

  const submit = document.createElement("input");
  submit.type = "submit"

  const form = document.createElement("form");
  form.append(input, submit)

  form.onsubmit = () => {
    if (input.value.toUpperCase() === fQuest.correct_answer.toUpperCase()) {
      submit.style.backgroundColor = "green";
      alert.textContent = "Correct!";
      input.value = fQuest.correct_answer;
    } else {
      submit.style.backgroundColor = "red";
      alert.textContent = "Incorrect!";
    }
    return false
  }

  secFree.append(header, alert, form);
}

function listen() {
  initMultipleTrivia();
  initFreeTrivia();
}

document.addEventListener("DOMContentLoaded", listen);

/**
 * @typedef QuestData
 * @property {string} category
 * @property {string} type
 * @property {string} difficulty
 * @property {string} question
 * @property {string} correct_answer
 * @property {string[]} incorrect_answers
 */