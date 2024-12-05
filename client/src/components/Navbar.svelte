
<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, P } from 'flowbite-svelte';
  import { DarkMode } from 'flowbite-svelte';
  
  $: activeUrl = $page.url.pathname;
  let btnClass = 'text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg text-xl p-2';
</script>

<Navbar class="bg-green-100 dark:bg-gray-800 shadow-lg p-0 ">
  <!-- Navbar Brand -->
  <NavBrand href="/" class="flex items-center p-3 pl-6 ">
    <span class="text-xl font-bold text-black uppercase dark:text-white">
      Sistema HC
    </span>
  </NavBrand>

  <!-- Hamburger for mobile -->
  <NavHamburger class="lg:hidden text-white" />

  <!-- Navbar Links -->
  <NavUl {activeUrl} class="flex items-center space-x-8 ml-auto transition-all ease-in-out duration-300">
    <!-- Home Link -->
    <NavLi href="/" class="relative">
      <P class="font-medium text-gray-700 hover:text-green-500 dark:text-gray-200 dark:hover:text-red-500 transition-all pb-1 duration-300">
        Inicio
      </P>
      {#if activeUrl === '/'}
        <span class="absolute inset-x-0 bottom-0 h-1 bg-green-500 rounded-full dark:bg-red-500"></span>
      {/if}
    </NavLi>

    <!-- Historias Clínicas Link -->
    <NavLi href="/historias_clinicas" class="relative">
      <P class="font-medium text-gray-700 hover:text-green-500 dark:text-gray-200 dark:hover:text-red-500 transition-all pb-1">
        Historias Clínicas
      </P>
      {#if activeUrl === '/historias_clinicas'}
        <span class="absolute inset-x-0 bottom-0 h-1 bg-green-500 rounded-full dark:bg-red-500"></span>
      {/if}
    </NavLi>

    <!-- Nueva Historia Link -->
    <NavLi href="/historias_clinicas/create" class="relative">
      <P class="font-medium text-gray-700 hover:text-green-500 dark:text-gray-200 dark:hover:text-red-500 transition-all pb-1">
        Nueva Historia
      </P>
      {#if activeUrl === '/historias_clinicas/create'}
        <span class="absolute inset-x-0 bottom-0 h-1 bg-green-500 rounded-full dark:bg-red-500"></span>
      {/if}
    </NavLi>

    <!-- Dark Mode Toggle -->
    <NavLi class="flex items-center">
      <DarkMode {btnClass} 
        class="text-gray-500 dark:text-gray-400 hover:text-green-500 dark:hover:text-red-500 transition-all p-2 rounded-lg"
      />
    </NavLi>
  </NavUl>
</Navbar>
