<!-- Navbar al puro estilo de html -->
<script>
    import { onMount } from 'svelte';

    onMount(() => {
        console.log('navbar');
    });
</script>

<nav>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/acerca">Acerca</a></li>
        <li><a href="/contacto">Contacto</a></li>
    </ul>
</nav>


<style>
    nav {
        background-color: #333;
        color: white;
        padding: 0.5rem;
    }

    ul {
        display: flex;
        justify-content: space-around;
        list-style: none;
    }

    a {
        color: white;
        text-decoration: none;
    }
</style>
