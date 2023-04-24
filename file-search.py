import os

file_metadata = {}

for root, directories, files in os.walk('.'):
    for _file in files:
        absolute_path = os.path.join(root, _file)
        size = os.path.getsize(absolute_path)
        file_metadata[_file] = [absolute_path,size]

#print(file_metadata)
n_files = None
while n_files is None:
    try:
        n_files = int(input("Cuántos archivos, como máximo, desea ver?: "))
    except ValueError:
        print("Solo se reciben números. Intente de nuevo")
        
ordenar_str = None
while ordenar_str is None:
    try:
        ordenar_str =  int(input("Ordenar según\n 0- Ninguno\n 1- Ruta\n 2- Tamaño\n 3- Nombre de archivo"))
    except ValueError:
        print("Solo se reciben enteros. Intente de nuevo")
    columna = ordenar_str - 1
        
ordenar_str = None
if columna != -1:
    while (ordenar_str == None):
        ordenar_str =  str(input("Ordenar ascendente? (Y/N): ")).lower()
        if ordenar_str == "y":
            inverso = False
        elif ordenar_str == "n":
            inverso = True
        else:
            ordenar_str = None

count = 0

print("Item\tTamaño\t\tArchivo")

if columna == -1:
    informacion = file_metadata.items()
elif columna == 2:
    informacion = sorted(file_metadata.items(),key=lambda archivo: archivo[0], reverse=inverso)
else:
    informacion = sorted(file_metadata.items(),key=lambda archivo: archivo[1][columna], reverse=inverso)

for file, info in informacion:
    if count >= n_files:
        break
    count += 1
    print(f"{count}-\t{info[1]} \tBytes\t{file}")
