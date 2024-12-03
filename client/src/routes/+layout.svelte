
<script>
  import "../app.css";
  import Header from '../components/Header.svelte';
  import Footer from '../components/Footer.svelte';
  import Navbar from '../components/Navbar.svelte';
</script>

<div class="flex flex-col min-h-screen bg-gray-50">

    <!-- Navbar -->
    <Navbar class="bg-gray-900 text-white shadow-xl border-b-2 border-gray-800"/>

  <!-- Contenido principal -->
  <main class="bg-white p-8 mx-auto flex-1 max-w-screen-lg mt-10">
    <Header class="mb-10"/>
    <slot></slot>
  </main>

  <!-- Footer -->
  <Footer class="bg-gray-900 text-white py-6 text-center mt-10"/>
</div>
