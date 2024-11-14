<script>
import { onMount } from 'svelte';

import { page } from '$app/stores';
import { goto } from '$app/navigation';

import { createConsulta } from '../../api/consultas.api.js';


const param_id = $page.params.id;

let cc_laboratorio = '';
let estado_actual = '';
let indicaciones = '';

let historia_clinica ='';

function go_historias_paciente() {
    goto(`/historias_clinicas/paciente/${param_id}`);
}

// funcion asincrona para crear una nueva consulta
async function crearConsulta() {
    const nueva_consulta = {
        historia_clinica,
        cc_laboratorio,
        estado_actual,
        indicaciones,
    };

    const res = await createConsulta(nueva_consulta);
    console.log(res);

    // redirigir a historis clinicas
    go_historias_paciente();
}

onMount(async () => {
    historia_clinica = param_id;
});

</script>

<h2>Nueva Consulta</h2>
<form on:submit|preventDefault={crearConsulta}>
    <label for="historia_clinica">Historia Clinica</label>
    <input type="text" id="historia_clinica" bind:value={historia_clinica} required disabled>
    <br>

    <label for="cc_laboratorio">CC Laboratorio</label>
    <input type="text" id="cc_laboratorio" bind:value={cc_laboratorio} required>
    <br>

    <label for="estado_actual">Estado Actual</label>
    <input type="text" id="estado_actual" bind:value={estado_actual} required>

    <br>

    <label for="indicaciones">Indicaciones</label>
    <input type="text" id="indicaciones" bind:value={indicaciones} required>

    <br>
    
    <button type="submit">Crear Consulta</button>
</form>
<button on:click={go_historias_paciente}>Cancelar</button>


