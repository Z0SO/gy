<script>

export let consulta = [];


</script>


{#if consulta.length > 0}
    {#each consulta as item}
        <div>
            <h2>Consulta de control N° {item.id}</h2>
            <p>Estado actual: {item.estado_actual}</p>
            <p>Indicaciones: {item.indicaciones}</p>
            <p>Historia clínica: {item.historia_clinica}</p>
            <p>CC Laboratorio: {item.cc_laboratorio}</p>
        </div>
    {/each}
{:else}
    <p>No hay consultas de control para este paciente</p>
{/if}
