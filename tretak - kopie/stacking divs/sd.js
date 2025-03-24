const wrapper = document.querySelector(".wrapper");

for (let i = 0; i < 6; i++) {
  // document.createElement("názevprvku")
  let novyDiv = document.createElement("div");

  // přidány classy square novému prvku
  novyDiv.classList.add("square");

  // náhodná generace čísel (budou sloužit jako barvy)
  let r = Math.floor(Math.random() * 255);
  let g = Math.floor(Math.random() * 255);
  let b = Math.floor(Math.random() * 255);

  // tzv. template literal - aneb psaní kodu do stringu
  novyDiv.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

  // do divu wrapper přida nově vytvořený prvek
  wrapper.appendChild(novyDiv);
}
