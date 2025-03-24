<script>
    let elapsedTime = $state(0)

    // $effect(() => {setInterval(() => {elapsedTime++}), 1000})

    // callback fce, volá jinou funkci, volá funkci každých 1000 milisekund
    // setInterval(function() {elapsedTime++}, 1000)
    setInterval(() => {elapsedTime++}, 1000)

    
</script>


<p>Timer: {elapsedTime}</p>