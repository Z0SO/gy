
<script>
  // Importar los componentes que se utilizarán en todas las páginas
  import Header from '../components/Header.svelte';
  import Footer from '../components/Footer.svelte';
  import Navbar from '../components/Navbar.svelte';
</script>

<Navbar />

<main>
  <Header />
  <slot />
  <Footer />
</main>



<style>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
    font-family: Arial, sans-serif;
}

</style>
