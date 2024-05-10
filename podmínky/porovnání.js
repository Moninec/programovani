let prvni = parseInt(prompt("První číslo"))
let druhy = parseInt(prompt("Druhé číslo"))

// int pracuje jen s celýma číslama, float - desetinná


if (prvni > druhy) {
    console.log("první je větší")
    alert ("první je větší")
} else if (druhy > prvni) {
    console.log("Druhý je větší než první")
    alert ("Druhý je větší než první")
} else if (prvni === druhy) {
    console.log("Čísla se rovnají")
    alert ("Čísla se rovnají")
}
