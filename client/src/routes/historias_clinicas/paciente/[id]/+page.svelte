<script>
import { onMount } from 'svelte';

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


// --- onMount
onMount(() => {
    fetchConsulta();
    fetchHistoriaClinica();
});


</script>


<h3>Paciente ID {param_id}</h3>

<TablaHistoriaClinicaDePaciente historia_clinica={una_historia_clinica} />

<hr>


<TablaConsultasDePaciente consulta={una_consulta} />
