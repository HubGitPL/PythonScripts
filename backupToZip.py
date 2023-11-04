import zipfile, os
from pathlib import Path
def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print(f'Tworzenie archiwum {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
        #spacer po katalogach
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Dodawanie plików w {foldername}...')
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Gotowe')

backupToZip(Path.home() / 'PycharmProjects')
