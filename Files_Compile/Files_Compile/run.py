import os
from dotenv import load_dotenv
import re

load_dotenv()
_directories = []
_printOutputs = False
_printableFiles = []

def Main():
    _directories = GetAllDirectoriesInDirectory(os.path.normpath(os.getenv("WORKING_DIRECTORY")))
    for i in _directories:
        for j in GetAllFilesInDirectory(i):
            printablefile = PrintableFile()
            printablefile.Directory = os.path.normpath(i)
            printablefile.NewDirectory = os.path.normpath(f'{os.getenv("OUTPUT_DIRECTORY")}')
            printablefile.FileName = j["FileName"]
            printablefile.NewFileName = f'{os.path.basename(i)}.txt'
            printablefile.FileLines = GetAllLinesInFile(j["Directory"], j["FileName"])
            _printableFiles.append(printablefile)
    
    for k in _printableFiles:
        k.Print()
        k.Write()

        


def GetAllDirectoriesInDirectory(directory):
    if _printOutputs:
        print('Getting directory list in directory ' + directory)

    directories = []

    for root, dirs, files in os.walk(directory):
        for name in dirs:
            directories.append(os.path.join(root, name))

    return directories


def GetAllFilesInDirectory(directory):
    if _printOutputs:
        print('Getting file list in directory ' + directory)
    fileList = []
    for filename in os.listdir(directory):
        i = os.path.join(directory, filename)
        if(os.path.isfile(i)):
            addition = dict(Directory = directory, FileName = filename)
            fileList.append(addition)
    if _printOutputs:
        for j in fileList:
            print('File: ' + j["FileName"] + ' found')
    return fileList
    

def GetAllLinesInFile(fileDirectory, fileName):
    if _printOutputs:
        print('Getting all lines in file ' + fileDirectory + '/' + fileName)
    with open(fileDirectory + '/' + fileName) as f:
        return f.readlines()


class PrintableFile:
    def __init__(self) -> None:
        Directory = ''
        NewDirectory = ''
        FileName = ''
        NewFileName = ''
        FileLines = []

    def Write(self):
        if _printOutputs:
            print(f'Writing list to file {self.Directory}\{self.FileName}')

        doesExist = os.path.exists(f'{self.NewDirectory}\{self.NewFileName}')
        with open(f'{self.NewDirectory}\{self.NewFileName}', 'a' if doesExist else 'w') as f:
            num = re.search('\d+', self.FileName)
            print(num)
            if num:
                f.write(f'\n\n\n--{num.group(0)}\n\n')
            for i in self.FileLines:
                f.write(f'{i.rstrip()}\n')
            f.close()

    def Print(self):
        print(f'Directory: {self.Directory}\nNewDirectory: {self.NewDirectory}\nFileName: {self.FileName}\nNewFileName: {self.NewFileName}\n')


Main()