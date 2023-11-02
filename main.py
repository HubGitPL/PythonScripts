import shutil, os
from pathlib import Path

p=Path.home() / 'studia'
#shutil.copy(p / 'spam.txt', p / 'Downloads')
#kopiuje zawartosc spam.txt do podanego folderu i zmienia jego nazwe
#shutil.copy(p / 'spam.txt', p / 'Downloads/spam2.txt')
#kopiuje cały katalog w inne miejsce
#hutil.copytree(p / 'Public', p / 'Downloads/public')

for folderName, subfolders, filenames in os.walk(p):
    print("Katalog bieżący to: " + folderName)

    for subfolder in subfolders:
        print(f'PODKATALOG KATALOGU {folderName}: ' + subfolder)

    for filename in filenames:
        print(f'PLIK KATALOGU {folderName}: ' + filename)
    print('')
