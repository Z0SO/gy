<script>
import { onMount } from 'svelte';
import { goto } from '$app/navigation';
import { page } from '$app/stores';
import { getConsultasByHistoriaClinica } from '../api/consultas.api.js';
import { getHistoriaById } from '../../api/historias.api.js';

import TablaHistoriaClinicaDePaciente from '../components/TablaHistoriaClinicaDePaciente.svelte';
import TablaConsultasDePaciente from '../components/TablaConsultasDePaciente.svelte';

let una_consulta = [];
let una_historia_clinica = [];
const param_id = $page.params.id;

async function fetchConsulta() {
    una_consulta = await getConsultasByHistoriaClinica(param_id);
    console.log(una_consulta);
}

async function fetchHistoriaClinica() {
    una_historia_clinica = await getHistoriaById(param_id);
    console.log(una_historia_clinica);
}
onMount(() => {
    fetchConsulta();
    fetchHistoriaClinica();
});
</script>


<TablaHistoriaClinicaDePaciente historia_clinica={una_historia_clinica} />

<div>
    separador de informacion
</div>

<TablaConsultasDePaciente consulta={una_consulta} />

<style>
div {
    background-color: #02040f;
}
</style>
