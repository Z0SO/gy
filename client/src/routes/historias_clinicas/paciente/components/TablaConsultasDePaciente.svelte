<script>
// import { onMount } from 'svelte';
import { deleteConsulta } from '../api/consultas.api.js';

import { goto } from '$app/navigation';

export let consulta = [];

const eliminarConsulta = async (id) => {
    try {
        const res = await deleteConsulta(id);
        console.log(res);
    } catch (error) {
        console.log(error);
    }
    //recargamos la pagna
    location.reload();
}

const alertDelete = (id) => {
    const confirmar = confirm('¿Está seguro que desea eliminar la consulta N° ' + id + '?');
    if (confirmar) {
        eliminarConsulta(id);
        console.log('Consulta eliminada');
    }
}

const go_editar_consulta = (id) => {
    goto(`/historias_clinicas/paciente/editar_consulta/${id}`);
}

</script>

{#if consulta.length > 0}
    {#each consulta as item}
        <div>
            <h2>Consulta de control N° {item.id}</h2>
            <p>Estado actual: {item.estado_actual}</p>
            <p>Indicaciones: {item.indicaciones}</p>
            <p>Historia clínica: {item.historia_clinica}</p>
            <p>CC Laboratorio: {item.cc_laboratorio}</p>
            <p>Fecha de la consulta: <b>{item.fecha_evaluacion}</b></p>
            <!-- para eliminar consulta -->
            <button
                on:click={() => alertDelete(item.id) }
            >Eliminar Consulta</button>
            <!-- para editar consulta -->
            <button
                on:click={() => go_editar_consulta(item.id) }
            >Editar Consulta</button>
            
        </div>
    {/each}
{:else}
    <p>No hay consultas de control para este paciente</p>
{/if}
