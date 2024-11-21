<script>
import { onMount } from 'svelte';
import { getHistorias } from '../api/historias.api.js';
import { goto } from '$app/navigation';

let historias = [];

const irAHistoria = (id) => {
    goto(`/historias_clinicas/paciente/${id}`);
}

onMount(
    async () => {
        historias = await getHistorias();
    }
);


console.log(historias);

</script>

{#if historias.length > 0}
    <table>
        <thead>
            <tr>
                <th>DNI</th>
                <th>Nombre</th>
                <th>Edad</th>
                <th>Domicilio</th>
                <th>Obra Social</th>
                <th>Teléfono</th>
                <th>Teléfono de Emergencia</th>
                <th>Ocupación</th>
                <th>Estado Civil</th>
                <th>Motivo de Consulta</th>
                <th>Derivado por</th>
                <th>Antecedentes Clínicos</th>
                <th>Estudios de Laboratorio</th>
                <th>Diagnóstico Presuntivo</th>
                <th>Tratamientos Anteriores</th>
                <th>Tratamiento Actual</th>
                <th>Fecha de Creación</th>
            </tr>
        </thead>
        <tbody>
            {#each historias as historia}
                <tr 
                on:click={() => irAHistoria(historia.id)}
                class="hoverHist"
                >
                    <td>{historia.pac_dni}</td>
                    <td>{historia.pac_nombre}</td>
                    <td>{historia.pac_edad}</td>
                    <td>{historia.pac_domicilio}</td>
                    <td>{historia.pac_obrasocial}</td>
                    <td>{historia.pac_telefono}</td>
                    <td>{historia.pac_telefono_emergencia}</td>
                    <td>{historia.pac_ocupacion}</td>
                    <td>{historia.pac_estadocivil}</td>
                    <td>{historia.motivo_consulta}</td>
                    <td>{historia.derivado_por}</td>
                    <td>{historia.antecedentes_clinicos}</td>
                    <td>{historia.hc_laboratorio}</td>
                    <td>{historia.diagnostico_presuntivo}</td>
                    <td>{historia.tratamientos_anteriores}</td>
                    <td>{historia.tratamiento_actual}</td>
                    <td>{historia.fecha_creacion}</td>
                </tr>
            {/each}
        </tbody>
    </table>
{:else}
    <p>No hay historias clínicas para mostrar</p>
{/if}


<style>
    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    .hoverHist:hover {
        background-color: #d1d1d1;
    }
</style>
