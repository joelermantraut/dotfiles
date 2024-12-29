#!/bin/bash

# Directorio donde está el entorno virtual y el script de Python
DIR="/home/joel/.config/scripts/switchto/"

# Nombre del entorno virtual
VENV_DIR="$DIR"

# Nombre del script de Python
PYTHON_SCRIPT="switchto.py"

# Cambiar al directorio especificado
cd "$DIR" || {
  echo "Directorio no encontrado"
  exit 1
}

# Activar el entorno virtual
if [ -d "$VENV_DIR" ]; then
  source "$VENV_DIR/bin/activate"
  echo "Entorno virtual activado"
else
  echo "Entorno virtual no encontrado en $VENV_DIR"
  exit 1
fi

# Ejecutar el script de Python
python "$PYTHON_SCRIPT" "$@"

# Desactivar el entorno virtual al terminar
deactivate
