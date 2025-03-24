<script>
	import Autoclicker from "$lib/components/Autoclicker.svelte";
	import Emoji from "$lib/components/Emoji.svelte";
	import Timer from "$lib/components/Timer.svelte";
	import Upgrade from "$lib/components/Upgrade.svelte";
    import { shared } from "$lib/shared.svelte";

    // let shared.count = $state(0)
    let animPop = $state()
    let btnAnim = $state()

    const colors = ["#FF00FF", "#6495ED", "#B22222", "#00FF00", "#8B008B"]
    let selectedColor = $state(colors[0])

    function increment(){
        shared.count = shared.count + shared.multi
        btnAnim = "btn-anim"

        setTimeout(() => {
            btnAnim = ""
            
        }, 100)
        
    }

    $effect(() => {
        if (shared.count > 0){
            animPop = "anim-pop" 
        }

        setTimeout(() => {
            animPop = ""
            
        }, 100)
    })
</script>

<Timer />
<Autoclicker />
<Upgrade upgradeLevel={1}/> 
<Upgrade upgradeLevel={2}/>
<Upgrade upgradeLevel={3}/>
<Emoji />
<!-- upgradeLevel - properties ($props()) -->

{#each colors as color}
<button class="vapo" onclick={() => selectedColor = color} aria-label={color} style="--color: {color}"></button>
{/each}

<div class="wrapper">
    <p class={animPop}>{shared.count}</p>
    <button class="btn {btnAnim}" onclick={increment} style="--color: {selectedColor}">Click meeeeeee</button>
</div>



<style>
    .wrapper{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        min-height: 100vh;
        gap: 1em;
    }
    .btn {
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background: var(--color, rebeccapurple);
        color: white;
    }

    .anim-pop{
        animation: popout 0.1s;
    }

    .btn-anim{
        animation: btn-anim 0.1s;
    }

    .vapo{
        --color: "lime";
        aspect-ratio: 1/1;
        height: 50px;
        border-radius: 50%;
        background-color: var(--color);
    }

    @keyframes popout{
        50% {
            scale: 5;
        }
        100% {
            scale: 1;
        }
    }

    @keyframes btn-anim{
        100%{
            scale: 0.9;
        }
        
    }
</style>
