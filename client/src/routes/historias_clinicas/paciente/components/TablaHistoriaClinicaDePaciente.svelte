<script>
export let historia_clinica = [];
</script>

<h3>Historia Clinica del Paciente {historia_clinica.pac_nombre}</h3>

<table class="table table-striped">
    <thead>
        <tr>
            <th scope="col">DNI</th>
            <th scope="col">Nombre</th>
            <th scope="col">Edad</th>
            <th scope="col">Domicilio</th>
            <th scope="col">Obra Social</th>
            <th scope="col">Telefono</th>
            <th scope="col">Telefono de Emergencia</th>
            <th scope="col">Ocupacion</th>
            <th scope="col">Estado Civil</th>
            <th scope="col">Motivo de Consulta</th>
            <th scope="col">Derivado por</th>
            <th scope="col">Antecedentes Clinicos</th>
            <th scope="col">Laboratorio</th>
            <th scope="col">Diagnostico Presuntivo</th>
            <th scope="col">Tratamientos Anteriores</th>
            <th scope="col">Tratamiento Actual</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{historia_clinica.pac_dni}</td>
            <td>{historia_clinica.pac_nombre}</td>
            <td>{historia_clinica.pac_edad}</td>
            <td>{historia_clinica.pac_domicilio}</td>
            <td>{historia_clinica.pac_obrasocial}</td>
            <td>{historia_clinica.pac_telefono}</td>
            <td>{historia_clinica.pac_telefono_emergencia}</td>
            <td>{historia_clinica.pac_ocupacion}</td>
            <td>{historia_clinica.pac_estadocivil}</td>
            <td>{historia_clinica.motivo_consulta}</td>
            <td>{historia_clinica.derivado_por}</td>
            <td>{historia_clinica.antecedentes_clinicos}</td>
            <td>{historia_clinica.hc_laboratorio}</td>
            <td>{historia_clinica.diagnostico_presuntivo}</td>
            <td>{historia_clinica.tratamientos_anteriores}</td>
            <td>{historia_clinica.tratamiento_actual}</td>
        </tr>
    </tbody>
</table>





