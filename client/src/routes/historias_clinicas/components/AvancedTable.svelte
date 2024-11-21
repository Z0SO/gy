<script>
  import { onMount } from 'svelte';
  import {
    Table,
    TableBody,
    TableBodyCell,
    TableBodyRow,
    TableHead,
    TableHeadCell,
  } from 'flowbite-svelte';

  import { getHistorias } from '../api/historias.api.js';
  import { goto } from '$app/navigation';

  let historias = [];

  const irAHistoria = (id) => {
    goto(`/historias_clinicas/paciente/${id}`);
  };

  onMount(async () => {
    historias = await getHistorias();
    console.log('Historias cargadas:', historias);
  });

  const sortByDate = (a, b) =>
    new Date(a.fecha_creacion) - new Date(b.fecha_creacion);
</script>

{#if historias.length > 0}
  <Table hoverable={true}>
    <TableHead>
      <TableHeadCell>DNI</TableHeadCell>
      <TableHeadCell>Nombre</TableHeadCell>
      <TableHeadCell>Edad</TableHeadCell>
      <TableHeadCell>Domicilio</TableHeadCell>
      <TableHeadCell>Obra Social</TableHeadCell>
      <TableHeadCell>Teléfono</TableHeadCell>
      <TableHeadCell>Teléfono de Emergencia</TableHeadCell>
      <TableHeadCell>Ocupación</TableHeadCell>
      <TableHeadCell>Estado Civil</TableHeadCell>
      <TableHeadCell>Motivo de Consulta</TableHeadCell>
      <TableHeadCell>Derivado por</TableHeadCell>
      <TableHeadCell>Antecedentes Clínicos</TableHeadCell>
      <TableHeadCell>Estudios de Laboratorio</TableHeadCell>
      <TableHeadCell>Diagnóstico Presuntivo</TableHeadCell>
      <TableHeadCell>Tratamientos Anteriores</TableHeadCell>
      <TableHeadCell>Tratamiento Actual</TableHeadCell>
      <TableHeadCell sort={sortByDate} defaultDirection="asc">
        Fecha de Creación
      </TableHeadCell>
    </TableHead>
    <TableBody tableBodyClass="divide-y">
      {#each historias as item}
        <TableBodyRow on:click={() => irAHistoria(item.id)}>
          <TableBodyCell>{item.pac_dni}</TableBodyCell>
          <TableBodyCell>{item.pac_nombre}</TableBodyCell>
          <TableBodyCell>{item.pac_edad}</TableBodyCell>
          <TableBodyCell>{item.pac_domicilio}</TableBodyCell>
          <TableBodyCell>{item.pac_obrasocial}</TableBodyCell>
          <TableBodyCell>{item.pac_telefono}</TableBodyCell>
          <TableBodyCell>{item.pac_telefono_emergencia}</TableBodyCell>
          <TableBodyCell>{item.pac_ocupacion}</TableBodyCell>
          <TableBodyCell>{item.pac_estadocivil}</TableBodyCell>
          <TableBodyCell>{item.motivo_consulta}</TableBodyCell>
          <TableBodyCell>{item.derivado_por}</TableBodyCell>
          <TableBodyCell>{item.antecedentes_clinicos}</TableBodyCell>
          <TableBodyCell>{item.hc_laboratorio}</TableBodyCell>
          <TableBodyCell>{item.diagnostico_presuntivo}</TableBodyCell>
          <TableBodyCell>{item.tratamientos_anteriores}</TableBodyCell>
          <TableBodyCell>{item.tratamiento_actual}</TableBodyCell>
          <TableBodyCell>{item.fecha_creacion}</TableBodyCell>
        </TableBodyRow>
      {/each}
    </TableBody>
  </Table>
{:else}
  <p>No hay historias clínicas para mostrar</p>
{/if}


