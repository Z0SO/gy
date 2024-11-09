#!/bin/bash

tput civis

# colores

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[0;33m'
readonly BLUE='\033[0;34m'
readonly PURPLE='\033[0;35m'
readonly CYAN='\033[0;36m'
readonly WHITE='\033[0;37m'
readonly BLACK='\033[0;30m'
readonly BOLD='\033[1m'
readonly END='\033[0m'

function ctrl_c() {
    echo -e "\n${RED}[*] Saliendo...${END}"
    tput cnorm
    exit 1
}

trap ctrl_c INT

function init() {
    echo -e "\n${GREEN}[~] --------------------------------------------------- [~]${END}"
    echo -e "${GREEN}[~] Script de inicializacion de entrorno de trabajo${END}"
    echo -e "${GREEN}[~] --------------------------------------------------- [~]${END}\n"
    sleep 0.5
    echo -e "${YELLOW}[!] Encendiendo entorno venv...${END}\n"
    source venv/bin/activate
   
    echo -e "${YELLOW}[!] Aplicando migraciones...${END}\n"
    python3 manage.py migrate

    echo -e "${YELLOW}[!] Iniciando servidor de desarrollo...${END}\n"
    python3 manage.py runserver
}

init
tput cnorm
