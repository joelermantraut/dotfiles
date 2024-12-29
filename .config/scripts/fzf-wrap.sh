#!/bin/sh

# Verificar herramientas necesarias
for cmd in "snap run alacritty" fzf find thunar; do
  if ! command -v $(echo $cmd | awk '{print $1}') >/dev/null 2>&1; then
    echo "Error: '$cmd' no está instalado o no es accesible en el PATH."
    exit 1
  fi
done

# Directorios de búsqueda
search_dirs="$@"
[ -z "$search_dirs" ] && search_dirs="."

# Crear un archivo temporal único
temp_file=$(mktemp)

# Ejecutar fzf en Alacritty usando /bin/sh
snap run alacritty --title fzf --class fzf -e /bin/sh -c "selected_file=\$(find $search_dirs -type f | fzf --exact --preview 'cat {}'); echo \$selected_file > $temp_file"
selected_file=$(cat "$temp_file")
rm "$temp_file"

# Verificar selección
if [ -z "$selected_file" ]; then
  echo "No se seleccionó ningún archivo."
  exit 1
fi

# Obtener el directorio del archivo seleccionado
selected_dir=$(dirname "$selected_file")

# Abrir explorador de archivos en el directorio seleccionado
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$selected_dir"
elif command -v thunar >/dev/null 2>&1; then
  pkill -x thunar
  thunar "$selected_dir"
else
  echo "Error: No hay un explorador de archivos compatible disponible."
  exit 1
fi
