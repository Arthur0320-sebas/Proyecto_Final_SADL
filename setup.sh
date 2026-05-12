#!/bin/bash

# ==========================================================
# Script de Configuración Inicial del Entorno (DevOps)
# Este script instala las herramientas base requeridas para
# la administración, desarrollo y despliegue del proyecto.
# ==========================================================

echo "--- Iniciando actualización del sistema ---"
sudo yum update -y

echo "--- Instalando herramientas de administración (Git y Vim) ---"
# Git para control de versiones y Vim para edición rápida en terminal
sudo yum install -y git vim

echo "--- Instalando motor de contenedores (Docker) ---"
# Docker es esencial para el despliegue del microservicio containerizado
sudo yum install -y docker

echo "--- Configurando y activando Docker ---"
sudo systemctl start docker
sudo systemctl enable docker
# Opcional: dar permisos al usuario actual para usar docker sin sudo
sudo usermod -a -G docker $USER

echo "--- Instalando Python 3 y librerías de AWS ---"
# Instalamos Python 3 y Boto3 para la automatización con Python
sudo yum install -y python3
pip3 install boto3

echo "--- Verificación de versiones ---"
git --version
docker --version
python3 --version

echo "--- Configuración finalizada con éxito ---"