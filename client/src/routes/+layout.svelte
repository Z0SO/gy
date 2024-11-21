
<script>
  import "../app.css";
  import Header from '../components/Header.svelte';
  import Footer from '../components/Footer.svelte';
  import Navbar from '../components/Navbar.svelte';
</script>

<div class="flex flex-col min-h-screen bg-gray-100">
  <!-- Navbar -->
  <Navbar class="bg-gray-800 text-white shadow-md"/>

  <!-- Contenido principal -->
  <main class="bg-white p-6  mx-auto flex-1">
    <Header />
    <slot></slot>
  </main>

  <!-- Footer -->
  <Footer class="bg-gray-800 text-white py-4 text-center"/>
</div>
