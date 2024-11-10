<script>
// formulario para crear una historia clinica

import { onMount } from 'svelte';
import { createHistoria } from '../api/historias.api.js';
import { goto } from '$app/navigation';


let historia = {
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

function submitForm() {
    createHistoria(historia);
    goto('/historias_clinicas');
}


</script>

<h2>
    Crear Historia Clínica
</h2>

<form on:submit|preventDefault="{submitForm}">
    <label for="pac_dni">DNI</label>
    <input type="text" id="pac_dni" bind:value="{historia.pac_dni}" required>
    <br>

    <label for="pac_nombre">Nombre</label>
    <input type="text" id="pac_nombre" bind:value="{historia.pac_nombre}" required>

    <br>

    <label for="pac_edad">Edad</label>
    <input type="text" id="pac_edad" bind:value="{historia.pac_edad}" required>

    <br>

    <label for="pac_domicilio">Domicilio</label>
    <input type="text" id="pac_domicilio" bind:value="{historia.pac_domicilio}" required>
    <br>


    <label for="pac_obrasocial">Obra Social</label>
    <input type="text" id="pac_obrasocial" bind:value="{historia.pac_obrasocial}" required>
    <br>


    <label for="pac_telefono">Teléfono</label>
    <input type="text" id="pac_telefono" bind:value="{historia.pac_telefono}" required>
    <br>


    <label for="pac_telefono_emergencia">Teléfono de Emergencia</label>
    <input type="text" id="pac_telefono_emergencia" bind:value="{historia.pac_telefono_emergencia}" required>
    <br>


    <label for="pac_ocupacion">Ocupación</label>
    <input type="text" id="pac_ocupacion" bind:value="{historia.pac_ocupacion}" required>
    <br>


    <label for="pac_estadocivil">Estado Civil</label>
    <input type="text" id="pac_estadocivil" bind:value="{historia.pac_estadocivil}" required>
    <br>


    <label for="motivo_consulta">Motivo de Consulta</label>
    <input type="text" id="motivo_consulta" bind:value="{historia.motivo_consulta}" required>
    <br>


    <label for="derivado_por">Derivado por</label>
    <input type="text" id="derivado_por" bind:value="{historia.derivado_por}" required>
    <br>


    <label for="antecedentes_clinicos">Antecedentes Clínicos</label>
    <input type="text" id="antecedentes_clinicos" bind:value="{historia.antecedentes_clinicos}" required>
    <br>


    <label for="hc_laboratorio">Estudios de Laboratorio</label>
    <input type="text" id="hc_laboratorio" bind:value="{historia.hc_laboratorio}" required>
    <br>


    <label for="diagnostico_presuntivo">Diagnóstico Presuntivo</label>
    <input type="text" id="diagnostico_presuntivo" bind:value="{historia.diagnostico_presuntivo}" required>
    <br>


    <label for="tratamientos_anteriores">Tratamientos Anteriores</label>
    <input type="text" id="tratamientos_anteriores" bind:value="{historia.tratamientos_anteriores}" required>
    <br>


    <label for="tratamiento_actual">Tratamiento Actual</label>
    <input type="text" id="tratamiento_actual" bind:value="{historia.tratamiento_actual}" required>
    <br>


    <button type="submit">Crear Historia Clínica</button>
</form>
