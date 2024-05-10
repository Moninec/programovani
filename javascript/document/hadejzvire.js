let tlacitko = document.querySelector("#tlacitko");
let nadpis = document.getElementById("nadpis");

let input = document.querySelector("#input");

tlacitko.addEventListener("click", zmenNadpis);

let cislo = 14;

 function zmenNadpis(){
    let textInputu = input.value;
    nadpis.innerText = textInputu;
    if (textInputu > cislo){
        nadpis.innerText = "Moje číslo je menší :(";
    } if (textInputu < cislo){
        nadpis.innerText = "Moje číslo je větši :(";
    } if (textInputu === cislo){
        nadpis.innerText = "Juchuuuu";
    }

 }