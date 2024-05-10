let tlacitko = document.querySelector("#tlacitko");
let nadpis = document.getElementById("nadpis");

let input = document.querySelector("#input");

// querySelector - vsechno (musi se napsat #)
// getElementById - bere jenom id

nadpis.style.color = "black";
tlacitko.addEventListener("click", zmenNadpis);
//naslouchadlo :)

function zmenNadpis(){
    let textInputu = input.value;
    nadpis.style.color = "pink";
    nadpis.style.fontSize = "100px";
    nadpis.innerText = textInputu;
    if (textInputu === "otázka"){
        nadpis.innerText = "42";
    } else{
        nadpis.innerText = textInputu;
    }


}