
from zipfile import ZipFile
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

# Browse the file and extract it
path1 = filedialog.askopenfilename(title="choose", initialdir="C:\\")  # using tkinter, we make dialog box to get location
with ZipFile(path1, 'r') as file:
    file.printdir()
    file.extractall(path1[:-4])