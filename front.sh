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
    cd ..
    exit 1
}

trap ctrl_c INT

function init() {


    echo -e "\n${GREEN}[~] --------------------------------------------------- [~]${END}"
    echo -e "${GREEN}\t Script de inicializacion de entorno de Svelte${END}"
    echo -e "${GREEN}[~] -----------------------[${RED}Z0SO${END}${GREEN}]---------------------- [~]${END}\n"

    cd client
    npm run dev
}

init
tput cnorm
