<script>
import { onMount } from 'svelte';
import { goto } from '$app/navigation';
import { page } from '$app/stores';

import  { getConsultaById } from '../../api/consultas.api.js';

let param_id = $page.params.id;

let una_consulta = [];

const consutlta_a_editar = async (id) => {
    una_consulta = await getConsultaById(id);
    console.log(una_consulta);
}


onMount(() => {
    // console.log('page', $page);console.log('page', $page.params);console.log('page', $page.params.id);
    consutlta_a_editar(param_id);
   
    // ya tengo  la consulta falta ahora llevarla a los campos pertinentes de un formulario y efectuar el metodo put

});

</script>

Pagina Editar consulta con id N°: {param_id}
