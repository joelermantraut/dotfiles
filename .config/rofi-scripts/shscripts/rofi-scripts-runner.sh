#!/bin/bash

# Directorio donde buscar los scripts .sh
DIRECTORIO="$HOME/.config/scripts"

# Verificar que el directorio existe
if [ ! -d "$DIRECTORIO" ]; then
  echo "El directorio $DIRECTORIO no existe."
  exit 1
fi

# Obtener la lista de archivos .sh y extraer solo el basename
ARCHIVOS=$(find "$DIRECTORIO" -maxdepth 1 -type f -name "*.sh" -exec basename {} \;)

# Verificar que haya archivos .sh en el directorio
if [ -z "$ARCHIVOS" ]; then
  echo "No se encontraron scripts .sh en $DIRECTORIO."
  exit 1
fi

# Mostrar los archivos en un menú con rofi
SELECCION=$(echo "$ARCHIVOS" | rofi -dmenu -p "Selecciona un script:")

# Verificar si el usuario seleccionó un archivo
if [ -z "$SELECCION" ]; then
  echo "No seleccionaste ningún archivo."
  exit 0
fi

# Construir la ruta completa del archivo seleccionado
ARCHIVO_SELECCIONADO="$DIRECTORIO/$SELECCION"

# Solicitar parámetros opcionales para el script
PARAMETROS=$(rofi -dmenu -p "Introduce parámetros para $SELECCION (opcional):")

# Hacer ejecutable el script si no lo es
if [ ! -x "$ARCHIVO_SELECCIONADO" ]; then
  chmod +x "$ARCHIVO_SELECCIONADO"
fi

# Ejecutar el script con los parámetros introducidos
if [ -z "$PARAMETROS" ]; then
  "$ARCHIVO_SELECCIONADO"
else
  "$ARCHIVO_SELECCIONADO" $PARAMETROS
fi
