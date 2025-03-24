<script>
    import { shared } from "$lib/shared.svelte";
    function plusClick(){

        setInterval(() => {shared.count++}, 1000)
    }
    
</script>

<button class="clicker" onclick={plusClick}>plus bonus</button>

<style>
    .clicker{
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background: lime;
        color: white;
        padding: 0.25em 0.5em;
    }
</style>