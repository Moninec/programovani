function hlavinova(pravda) {
    console.log(pravda);
    console.log("smrdí");
}

hlavinova("Diana");
hlavinova("Julie");

function scitani(cisloA, cisloB) {
    let vysledek = cisloA + cisloB;
    console.log(vysledek);
}

//kdyz je promenna vr funkci - funguje jen v rámci funkce
//console.log(vysledek) nefunguje

scitani(3, 8);

function prevod(km) {
    let mile = km * 1.609;
    return mile;
    //return - muzu pracovat s promennou mimo funkci
}
prevod(10);

console.log(prevod(50));

ajaj;
