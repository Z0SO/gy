<script>
  import { page } from '$app/stores';
  import { Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
import {  CirclePlusSolid, ArchiveSolid } from 'flowbite-svelte-icons';
  $: activeUrl = $page.url.pathname;

let activeClass = 'flex items-center p-2 text-base font-normal text-green-700 dark:text-white ';

let nonActiveClass = 'flex items-center p-2 text-base font-normal text-green-900 dark:text-white ';
</script>

<Sidebar {activeUrl} {activeClass} {nonActiveClass}
    class="bg-green-50 dark:bg-gray-800 shadow-lg p-0 "
>
  <SidebarWrapper
        class="bg-green-100 dark:bg-gray-800"
    >
    <SidebarGroup>

        <!-- item para historias clinicas -->
      <SidebarItem label="Historias Clínicas" href="/historias_clinicas"
        class="hover:bg-green-200 dark:hover:bg-gray-700 rounded-lg"
      >

        <svelte:fragment slot="icon">
          <ArchiveSolid class="w-6 h-6" />
        </svelte:fragment>
      </SidebarItem>

      <!-- item para nueva historia -->
        <SidebarItem label="Nueva Historia" href="/historias_clinicas/create"
            class="hover:bg-green-200 dark:hover:bg-gray-700 rounded-lg"
        >
            <svelte:fragment slot="icon">
                <CirclePlusSolid class="w-6 h-6" />
            </svelte:fragment>
        </SidebarItem>



    </SidebarGroup>
  </SidebarWrapper>
</Sidebar>

