<script>

import { onMount } from 'svelte';
import { page } from '$app/stores';
import { goto } from '$app/navigation';

import { getHistoriaById } from '../../api/historias.api.js';
import { updateHistoria } from '../../api/historias.api.js';

const param_id = $page.params.id; // obtenemos el id de la url como parametro

let una_historia = {
    pac_dni: '',
    pac_nombre: '',
    pac_edad: '',
    pac_domicilio: '',
    pac_obrasocial: '',
    pac_telefono: '',
    pac_telefono_emergencia: '',
    pac_ocupacion: '',
    pac_estadocivil: '',
    motivo_consulta: '',
    derivado_por: '',
    antecedentes_clinicos: '',
    hc_laboratorio: '',
    diagnostico_presuntivo: '',
    tratamientos_anteriores: '',
    tratamiento_actual: ''
};

const goHistoriasPaciente = () => {
    goto(`/historias_clinicas/paciente/${param_id}`);
};

const actualizarHistoria = async () => {
    try {
        await updateHistoria(param_id, una_historia);
        goHistoriasPaciente();
    } catch (error) {
        console.error(`Error al actualizar la historia: ${error}`);
    }
};

onMount(async () => {
    una_historia = await getHistoriaById(param_id);
    console.log(una_historia);
});
</script>

<h2>Editar Historia Clínica</h2>

<form
    on:submit|preventDefault={ actualizarHistoria }
>
    <label for="pac_dni">DNI</label>
    <input type="text" id="pac_dni" bind:value={una_historia.pac_dni} required>
    <br>

    <label for="pac_nombre">Nombre</label>
    <input type="text" id="pac_nombre" bind:value={una_historia.pac_nombre} required>

    <br>

    <label for="pac_edad">Edad</label>
    <input type="text" id="pac_edad" bind:value={una_historia.pac_edad} required>

    <br>

    <label for="pac_domicilio">Domicilio</label>
    <input type="text" id="pac_domicilio" bind:value={una_historia.pac_domicilio} required>
    <br>

    <label for="pac_obrasocial">Obra Social</label>
    <input type="text" id="pac_obrasocial" bind:value={una_historia.pac_obrasocial} required>
    <br>

    <label for="pac_telefono">Teléfono</label>
    <input type="text" id="pac_telefono" bind:value={una_historia.pac_telefono} required>
    <br>

    <label for="pac_telefono_emergencia">Teléfono de Emergencia</label>
    <input type="text" id="pac_telefono_emergencia" bind:value={una_historia.pac_telefono_emergencia} required>
    <br>

    <label for="pac_ocupacion">Ocupación</label>
    <input type="text" id="pac_ocupacion" bind:value={una_historia.pac_ocupacion} required>
    <br>

    <label for="pac_estadocivil">Estado Civil</label>
    <input type="text" id="pac_estadocivil" bind:value={una_historia.pac_estadocivil} required>
    <br>

    <label for="motivo_consulta">Motivo de Consulta</label>
    <input type="text" id="motivo_consulta" bind:value={una_historia.motivo_consulta} required>
    <br>

    <label for="derivado_por">Derivado por</label>
    <input type="text" id="derivado_por" bind:value={una_historia.derivado_por} required>
    <br>

    <label for="antecedentes_clinicos">Antecedentes Clinicos</label>
    <input type="text" id="antecedentes_clinicos" bind:value={una_historia.antecedentes_clinicos} required>
    <br>

    <label for="hc_laboratorio">Laboratorio</label>
    <input type="text" id="hc_laboratorio" bind:value={una_historia.hc_laboratorio} required>
    <br>

    <label for="diagnostico_presuntivo">Diagnostico Presuntivo</label>
    <input type="text" id="diagnostico_presuntivo" bind:value={una_historia.diagnostico_presuntivo} required>
    <br>

    <label for="tratamientos_anteriores">Tratamientos Anteriores</label>
    <input type="text" id="tratamientos_anteriores" bind:value={una_historia.tratamientos_anteriores} required>
    <br>

    <label for="tratamiento_actual">Tratamiento Actual</label>
    <input type="text" id="tratamiento_actual" bind:value={una_historia.tratamiento_actual} required>
    <br>

    <button type="submit">Actualizar Historia Clínica</button>
</form>
<button on:click={goHistoriasPaciente}>Volver</button>

