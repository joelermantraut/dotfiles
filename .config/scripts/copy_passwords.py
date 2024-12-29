import csv
import subprocess

# Nombre del archivo CSV
csv_file = "/media/joel/DEBIAN 12_8/keys.csv"


def main():
    # Leer el archivo CSV
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Iterar sobre cada fila del CSV
        for row in reader:
            group = row["Group"]
            title = row["Title"]
            username = row["Username"]
            password = row["Password"]

            # Crear el nombre de la entrada en pass
            if group == "Raíz":
                pass_entry_name = f"{title}"
            else:
                pass_entry_name = f"{group}/{title}"

            # Preparar el comando para insertar la contraseña
            command = f'echo "{password}\n{password}" | pass insert "{pass_entry_name}"'

            # Ejecutar el comando
            try:
                result = subprocess.run(
                    command,
                    shell=True,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                print(f"Contraseña para {title} agregada con éxito.")
            except subprocess.CalledProcessError as e:
                print(
                    f"Error al agregar la contraseña para {title}: {e.stderr.decode().strip()}"
                )


if __name__ == "__main__":
    main()
