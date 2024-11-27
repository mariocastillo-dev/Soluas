#!/bin/bash

# Actualizar el sistema
sudo apt update

# Instalar MySQL Server
sudo apt install -y mysql-server

# Instalar Python 3 y Pip (si no están ya instalados)
sudo apt install -y python3 python3-pip python3-venv

# Crear un entorno virtual llamado 'soluas'
python3 -m venv soluas

# Activar el entorno virtual
source soluas/bin/activate

# Actualizar pip dentro del entorno virtual
pip install --upgrade pip

# Instalar todas las dependencias de Python usando requirements.txt
pip install -r requirements.txt

echo "Setup completado. El entorno virtual está listo y las dependencias están instaladas."
