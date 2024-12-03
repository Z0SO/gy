
<script>
  import { Alert } from 'flowbite-svelte';
  import { InfoCircleSolid } from 'flowbite-svelte-icons';
</script>

<div class="px-8 py-10 mx-auto max-w-screen-xl">
  <!-- Alerta -->
  <Alert class="mb-8 border-l-4 border-blue-500 bg-blue-50 p-4">
    <InfoCircleSolid slot="icon" class="w-6 h-6 text-blue-600" />
    <span class="font-semibold text-blue-800">¡Alerta importante!</span>
    Modifica algunos detalles e intenta enviar de nuevo.
  </Alert>

  <!-- Contenido Principal -->
  <main>
    <h1 class="text-4xl font-extrabold text-gray-900 mb-6">Bienvenido a INICIO</h1>
    <p class="text-xl text-gray-700 leading-relaxed">
      Explora y gestiona las historias clínicas de manera sencilla y eficaz. Nuestro sistema está diseñado para ofrecerte una experiencia intuitiva y fluida.
    </p>
  </main>
</div>

<!-- <script> -->
<!--   import { Alert } from 'flowbite-svelte'; -->
<!--   import { InfoCircleSolid } from 'flowbite-svelte-icons'; -->
<!-- </script> -->

<!-- <Alert> -->
<!--   <InfoCircleSolid slot="icon" class="w-5 h-5" /> -->
<!--   <span class="font-medium">Default alert!</span> -->
<!--   Change a few things up and try submitting again. -->
<!-- </Alert> -->
<!-- <main> -->
<!--   <h1>INICIO</h1> -->
<!--     <span> -->
<!--         inicio -->
<!--     </span> -->
<!-- </main> -->
