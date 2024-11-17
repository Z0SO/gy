<script>
import { onMount } from 'svelte';
import { goto } from '$app/navigation';
import { page } from '$app/stores';

import { getConsultaById, updateConsulta } from '../../api/consultas.api.js';

let param_id = $page.params.id;
let una_consulta = {};
let cc_laboratorio = '';
let estado_actual = '';
let indicaciones = '';
let historia_clinica = '';

const consulta_a_editar = async (id) => {
    una_consulta = await getConsultaById(id);
    cc_laboratorio = una_consulta.cc_laboratorio;
    estado_actual = una_consulta.estado_actual;
    indicaciones = una_consulta.indicaciones;
    historia_clinica = una_consulta.historia_clinica;

    console.log(una_consulta);
    console.log(`DEBUG -> | ${cc_laboratorio} | ${estado_actual} | ${indicaciones} |`);
}

const actualizar_consulta = async () => {
    const consulta_actualizada = {
        cc_laboratorio,
        estado_actual,
        indicaciones,
        historia_clinica
    };
   
    try {
        await updateConsulta(param_id, consulta_actualizada); 
        goto_historiasClinicas(historia_clinica);
    } catch (error) {
        console.log(`Error al actualizar la consulta: ${error}`);
    }
}

const goto_historiasClinicas = (hc) => {
    goto(`/historias_clinicas/paciente/${hc}`);
}

onMount(() => {
    consulta_a_editar(param_id);
});
</script>

<h1>Pagina Editar consulta con id N°: {param_id}</h1>
<p>Paciente con id N°: {historia_clinica}</p>

<form on:submit|preventDefault={actualizar_consulta}>
    <label for="cc_laboratorio">CC Laboratorio</label>
    <input type="text" id="cc_laboratorio" bind:value={cc_laboratorio} required>
    <br>
    <label for="estado_actual">Estado Actual</label>
    <input type="text" id="estado_actual" bind:value={estado_actual} required>
    <br>
    <label for="indicaciones">Indicaciones</label>
    <input type="text" id="indicaciones" bind:value={indicaciones} required>
    <br>
    <button type="submit">Actualizar Consulta</button>
</form>

<button on:click={() => goto_historiasClinicas(historia_clinica)}>Cancelar</button>
