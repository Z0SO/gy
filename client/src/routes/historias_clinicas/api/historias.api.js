
// esta es el archivo que se encarga de manejar las rutas de la API de historias

import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/historias_clinicas';
// se crea una instancia de axios con la URL base de la API
const api = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const getHistorias = async () => {
    try {
        const response = await api.get('/');
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

export const getHistoriaById = async (id) => {
    try {
        const response = await api.get(`/${id}`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

export const createHistoria = async (historia) => {
    try {
        const response = await api.post('/', historia);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

export const updateHistoria = async (id, historia) => {
    try {
        const response = await api.put(`/${id}/`, historia);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

export const deleteHistoria = async (id) => {
    try {
        const response = await api.delete(`/${id}/`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}
