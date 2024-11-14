<script>
import { onMount } from 'svelte';

import { goto } from '$app/navigation';

// como vamos a usar la id que viene en la url, la traemos de la url
import { page } from '$app/stores';

// traemos la variable id de la url
import { getConsultasByHistoriaClinica } from '../api/consultas.api.js';

// traer el js de la api de historias clinicas para buscar la historia clinica por id y extraer el nombre
import { getHistoriaById } from "../../api/historias.api.js";

// <!-- importamos los componentes -->
import TablaHistoriaClinicaDePaciente from '../components/TablaHistoriaClinicaDePaciente.svelte';
import TablaConsultasDePaciente from '../components/TablaConsultasDePaciente.svelte';

// --- variables

let una_consulta = [];
let una_historia_clinica = [];

// traemos la id de la url
const param_id = $page.params.id;
//console.log(param_id);


// --- funciones
async function fetchConsulta() {
    una_consulta = await getConsultasByHistoriaClinica(param_id);
    console.log(una_consulta);
}

async function fetchHistoriaClinica() {
    una_historia_clinica = await getHistoriaById(param_id);
    console.log(una_historia_clinica);
}

function go_create_consulta() {
    goto(`/historias_clinicas/paciente/nueva_consulta/${param_id}`);
}

// --- onMount
onMount(() => {
    fetchConsulta();
    fetchHistoriaClinica();
});


</script>

<button
    on:click={go_create_consulta}
>
   Nueva Consulta
</button>


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
