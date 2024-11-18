<script>import "../app.css";
// Importar los componentes que se utilizarán en todas las páginas
import Header from '../components/Header.svelte';
import Footer from '../components/Footer.svelte';
import Navbar from '../components/Navbar.svelte';
</script>


<Navbar></Navbar>

<main>
  <Header></Header>
  <slot></slot>
  <Footer></Footer>
</main>
