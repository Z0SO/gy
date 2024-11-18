<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
</script>

<Navbar>
  <NavBrand href="/">
    <!-- <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" /> -->
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Sistema Historias Clinicas</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl}>
    <NavLi href="/">Home</NavLi>
    <NavLi href="/historias_clinicas">Historias Clínicas</NavLi>
    <NavLi href="/historias_clinicas/create">Nueva Historia</NavLi>
  </NavUl>
</Navbar>
<!-- <nav> -->
<!--     <ul> -->
<!--         <li><a href="/">Inicio</a></li> -->
<!--         <li><a href="/historias_clinicas">Historias Clínicas</a></li> -->
<!--         <li><a href="/historias_clinicas/create">Nueva Historia</a></li> -->
<!--     </ul> -->
<!-- </nav> -->


