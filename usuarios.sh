#!/bin/bash
sudo useradd devops_user
sudo groupadd devops_group
sudo usermod -aG devops_group devops_user
sudo chown -R devops_user:devops_group ~/environment
sudo chown -R ec2-user:ec2-user ~/environment
echo "Gestión de usuarios y permisos completada."
