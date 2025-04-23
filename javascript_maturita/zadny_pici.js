// let pici = ["quattro formaggi", "hawaii", "margherita", "vegetariana", "prosciutto"]

// for (let i = 0; i < pici.length; i++) {
//     console.log(pici[i])
    
// }

// for (let i = 0; i < 10; i++) {
//     console.log("Zadne pici :(")
    
// }

// pici.forEach(element => {
//     console.log(element)
// });



// for (const pica of pici) {
//     console.log(pica)
// }

// // u while cyklu dávat pozor na složené závorky
// // když chceme, aby se něco rovnalo, používáme ===, tři rovnítka rozlišuje string od čísel, dvě rovnítka ne

// let x = 3
// let y = "3"

// soucet = x + y
// console.log(soucet)

const nadpis = document.querySelector("#nadpis")
const tlacitko = document.querySelector(".button")
const tlacitko2 = document.querySelector(".button2")
const input = document.querySelector(".input")

//tlacitko.addEventListener("click", funkce) //kdyby se u funkce napsali závorky, spustí se ihned

tlacitko.addEventListener("click", function(){
    console.log("funkceeee")
    nadpis.innerText = "Učitel je suchar"
    nadpis.style.color = "purple"
    nadpis.style.fontSize = "100px"
    nadpis.classList.add("hokus") //přidá classu k prvku
})

// arrow function
// tlacitko.addEventListener("click", () => {
//     console.log("funkceeee")
// })


// function funkce(){
    
// }

tlacitko2.addEventListener("click", () => {
    console.log(input.value)
})



