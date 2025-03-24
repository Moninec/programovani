<script>
    import { shared } from "$lib/shared.svelte";
    let shopClicked = $state(false)

    let { upgradeLevel } = $props()

    
    function upCount(){
        shopClicked = !shopClicked
        
        if (upgradeLevel === 1){
            shared.multi = 2
        }else if (upgradeLevel === 2){
            shared.multi = 5
        }else if (upgradeLevel === 3){
            shared.multi = 10
        }

    }
        
        


</script>

<div>
    {#if shopClicked}
        <p>Shop upgraded</p>
    {:else}
    <p>Upgrade to {upgradeLevel}</p>
    {/if}
        
    <button class="btn2" onclick={upCount}>Upgrade</button>
</div>


<style>
    .btn2{
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background: green;
        color: white;
        padding: 0.25em 0.5em;

        transition: 0.5 linear;
    }

    .btn2:active{
        scale: 0.5s;
    }

    div{
        border: 2px solid #00baa5;
        padding: 0.5em 0.5em;
        margin: 5px;
        width: fit-content;
    }

</style>