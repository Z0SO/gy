<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, P } from 'flowbite-svelte';
  import { DarkMode } from 'flowbite-svelte';
  
  $: activeUrl = $page.url.pathname;
  let btnClass = 'text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg text-xl p-2';
</script>

<Navbar 
    class="bg-gray-200 m-0
>
    <NavBrand href="/" class="flex-grow bg-red-600 items-center p-3 pl-6 m-0">
        <span class="self-center whitespace-nowrap text-xl font-semibold text-green-600 uppercase dark:text-white">
            Sistema HC
        </span>
    </NavBrand>

  <NavHamburger />

  <NavUl {activeUrl}
    >
    <NavLi href="/">
           <P class="hover:text-green-500 font-semibold dark:hover:text-red-500">
                Inicio
            </P> 
        </NavLi>
    <NavLi href="/historias_clinicas">
           <P class="hover:text-green-500 font-semibold dark:hover:text-red-500">
                Historias Clinicas
            </P> 
        </NavLi>
    <NavLi href="/historias_clinicas/create">
           <P class="hover:text-green-500 font-semibold dark:hover:text-red-500">
                Nueva Historia
            </P> 
        </NavLi>
    <NavLi>
        <DarkMode {btnClass} 
            class="m-0 p-0 hover:bg-transparent hover:text-green-500 font-semibold dark:text-white dark:hover:text-red-500 dark:hover:bg-transparent" />
    </NavLi>
  </NavUl>
</Navbar>
<!-- <nav> -->
<!--     <ul> -->
<!--         <li><a href="/">Inicio</a></li> -->
<!--         <li><a href="/historias_clinicas">Historias Clínicas</a></li> -->
<!--         <li><a href="/historias_clinicas/create">Nueva Historia</a></li> -->
<!--     </ul> -->
<!-- </nav> -->


