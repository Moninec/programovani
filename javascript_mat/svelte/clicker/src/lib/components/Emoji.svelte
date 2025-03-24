<script>
    import { shared } from "$lib/shared.svelte";

    // let clicked = $state(false)

    // let { upgradeClick } = $props()

    function emojiPlus(){
        // shopClicked = !shopClicked
        shared.count = shared.count + Math.floor(Math.random() * (50 - 1 + 1)) + 1;
        
        // shared.count = shared.count + 50

    }
</script>

<button class="emoji" onclick={emojiPlus}>👾</button>

<style>
    .emoji{
        font-size: 50px;
    }
</style>

