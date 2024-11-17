
// archivo .api.js profesional de consulta control de historias clinicas con axios

import axios from 'axios';

//aqui la url de la api de django
const API_URL = 'http://localhost:8000/api/consultas_control/';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Para obtener todas las consultas (cosa que no se cuando podria pasar pero lo dejo aca)

export const getConsultas = async () => {
    try {
        const response = await api.get('/');
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Para obtener una consulta por id (cosa que si se va a usar y es crucial)
export const getConsultaById = async (id) => {
    try {
        const response = await api.get(`/${id}`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Para crear una nueva consulta desde el front
export const createConsulta = async (consulta) => {
    try {
        const response = await api.post('/', consulta);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}


// Para actualizar una consulta desde el front
export const updateConsulta = async (id, consulta) => {
    try {
        const response = await api.put(`${id}/`, consulta);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Para borrar una consulta desde el front
export const deleteConsulta = async (id) => {
    try {
        const response = await api.delete(`${id}/`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// para filtrar por aquiellas consultas cuyo campo historia_clinica coincida con el id de la historia clinica que se le pase
export const getConsultasByHistoriaClinica = async (id) => {
    try {
        const response = await api.get(`?historia_clinica=${id}`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

