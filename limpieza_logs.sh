#!/bin/bash
find ~/environment -name "*.log" -type f -mtime +7 -delete
echo "Limpieza de logs completada: $(date)"
