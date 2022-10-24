const gameboard = document.getElementById("gameboard");
const gametime = document.getElementById("gametime");
const gamepoints = document.getElementById("gamepoints");
const gameobj = {
  game: [],
  mathed: [],
  points: 0,
  time: 0,
  timestamp: Date.now()
}

/**
 * @param {string} gameTheme 
 */
function init(gameTheme) {
  gameobj.game = randomize(duplicate(GAME_THEMES[gameTheme]))

  const gametable = document.createElement("table")
  gametable.classList.add("table")

  const tbody = document.createElement("tbody")

  for (let i = 0; i < gameobj.game.length; i++) {
    const element = gameobj.game[i];

    const img = document.createElement("img")
    img.classList.add("m-1")
    img.setAttribute("src", element.src)
    img.setAttribute("img_id", element.id)
    img.setAttribute("img_src", element.src)
    img.setAttribute("id", i)

    tbody.appendChild(img)
  }

  gametable.appendChild(tbody)

  gameboard.append(gametable)

  setTimeout(() => {
    for (let i = 0; i < tbody.children.length; i++) {
      const element = tbody.children[i];

      element.setAttribute("src", "static/assets/question.png")

      element.addEventListener("click", () => {
        const secondId = element.getAttribute("id")

        if (gameobj.mathed.includes(secondId)) return

        if (gameobj.second) return

        if (gameobj.first) {
          if (gameobj.first === secondId) return

          gameobj.second = secondId

          const first = document.getElementById(gameobj.first)

          if (first.getAttribute("img_id") === element.getAttribute("img_id")) {
            gameobj.mathed.push(gameobj.first, gameobj.second)

            delete gameobj.first
            delete gameobj.second

            gamepoints.textContent = gameobj.points += 2

            if (gameobj.game.length === gameobj.mathed.length) {
              clearInterval(gameobj.timeInterval)

              const input0 = document.createElement("input")
              input0.classList.add("form-control")
              input0.setAttribute("name", "time")
              input0.setAttribute("type", "hidden")
              input0.setAttribute("value", gameobj.time)

              const input1 = document.createElement("input")
              input1.classList.add("form-control")
              input1.setAttribute("name", "points")
              input1.setAttribute("type", "hidden")
              input1.setAttribute("value", gameobj.points)

              const input = document.createElement("input")
              input.classList.add("form-control")
              input.setAttribute("autofocus", "")
              input.setAttribute("name", "username")
              input.setAttribute("type", "text")
              input.setAttribute("required", "")
              input.setAttribute("placeholder", "Name")

              const div = document.createElement("div")
              div.classList.add("form-group")
              div.appendChild(input)

              const button = document.createElement("button")
              button.setAttribute("type", "submit")
              button.classList.add("btn", "btn-primary")
              button.textContent = "Submit"

              const form = document.createElement("form")
              form.setAttribute("action", "/game")
              form.setAttribute("method", "post")
              form.append(input0, input1, div, button)

              gameboard.replaceChildren(form)
            }
          } else {
            setTimeout(() => {
              first.setAttribute("src", "static/assets/question_red.png")
              element.setAttribute("src", "static/assets/question_red.png")

              delete gameobj.first
              delete gameobj.second

              gamepoints.textContent = --gameobj.points
            }, 1000)
          }

          element.setAttribute("src", element.getAttribute("img_src"))
        } else {
          gameobj.first = element.getAttribute("id")

          element.setAttribute("src", element.getAttribute("img_src"))
        }
      })
    }

    gameobj.timeInterval = setInterval(() => {
      gametime.textContent = ++gameobj.time
    }, 1000)
  }, 3000)
}

/**
 * @param {any[]} array
 * @return {any[]}
 */
function duplicate(array) {
  return array.reduce((acc, cur) => acc.concat(cur, cur), []);
}

/**
 * @param {any[]} array
 * @return {any[]}
 */
function randomize(array) {
  return array.sort(() => Math.random() - 0.5);
}

const GAME_THEMES = {
  number: [
    {
      id: 1,
      src: "static/assets/number/asterisk.png",
    }, {
      id: 2,
      src: "static/assets/number/eight.png",
    }, {
      id: 3,
      src: "static/assets/number/five.png",
    }, {
      id: 4,
      src: "static/assets/number/four.png",
    }, {
      id: 5,
      src: "static/assets/number/nine.png",
    }, {
      id: 6,
      src: "static/assets/number/one.png",
    }, {
      id: 7,
      src: "static/assets/number/seven.png",
    }, {
      id: 8,
      src: "static/assets/number/six.png",
    }, {
      id: 9,
      src: "static/assets/number/ten.png",
    }, {
      id: 10,
      src: "static/assets/number/three.png",
    }, {
      id: 11,
      src: "static/assets/number/two.png",
    }, {
      id: 12,
      src: "static/assets/number/zero.png",
    },
  ]
}

init("number")