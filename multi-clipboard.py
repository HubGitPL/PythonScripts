from pathlib import Path
import os
#make sure to specify your folder_path!!!
folder_path = '/Users/mat/PycharmProjects/pythonProject'
if not os.path.exists(folder_path):
    print(f'Wybrana scieźka: {folder_path} NIE istnieje')
else:
    p = Path(folder_path)
    lista = list(p.glob('*.txt'))
    for listaI in lista:
        file_path = os.path.join(folder_path, listaI)
        try:
            os.remove(file_path)
            print(f"Usunięto: {file_path}")
        except OSError as e:
            print(f"Błąd podczas usuwania {file_path}: {e}")
print("Proces usuwania został zakończony")






