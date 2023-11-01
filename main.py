import shutil, os
from pathlib import Path

p=Path.home()
shutil.copy(p / 'spam.txt', p / 'Downloads')
#kopiuje zawartosc spam.txt do podanego folderu i zmienia jego nazwe
shutil.copy(p / 'spam.txt', p / 'Downloads/spam2.txt')
