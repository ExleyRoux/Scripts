from dotenv import load_dotenv
import os

load_dotenv()

_printOutputs = False

def Main():
    foundlist = []
    searchForFileList = GetAllLinesInFile(os.getenv("INPUT_FILE_DIRECTORY"), os.getenv("INPUT_FILE"))
    filesInFolderList = GetAllFilesInDirectory(os.getenv("WORKING_DIRECTORY"))

    for i in searchForFileList:
        for j in filesInFolderList:
            if not ( j["Directory"] == os.getenv("INPUT_FILE_DIRECTORY") and j["FileName"] == os.getenv("INPUT_FILE")) and not ( j["Directory"] == os.getenv("OUTPUT_FILE_DIRECTORY") and j["FileName"] == os.getenv("OUTPUT_FILE")):
                for k in GetAllLinesInFile(j["Directory"], j["FileName"]):
                    compare1 = CleanupString(i)
                    compare2 = CleanupString(k)
                    if Find(compare2, compare1):
                        foundlist.append(f'FOUND : \t{StripString(i)}\nIN STRING : \t{StripString(k)}\nIN FILE : \t{j["FileName"]}\n')

    WriteListToFile(os.getenv("OUTPUT_FILE_DIRECTORY"), os.getenv("OUTPUT_FILE"), foundlist)
    

def WriteListToFile(directory, filename, list):
    if _printOutputs:
        print(f'Writing list to file {directory}/{filename}')

    with open(os.getenv("WORKING_DIRECTORY") + '/' + os.getenv("OUTPUT_FILE"), 'w') as f:
        for i in list:
            f.write(f'{i}\n')
        f.close()


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


def PrintList(list):
    if _printOutputs:
        print('Printing list')

    for i in list:
        print(i)


def StripString(inputString):
    return inputString.strip()


def ToUpperString(inputString):
    return inputString.upper()


def ReplaceEmptyChars(inputString):
    return inputString.replace(' ', '')


def CleanupString(inputString):
    return ReplaceEmptyChars(ToUpperString(StripString(inputString)))


def Find(inputString, subString):
    if inputString.find(subString) > -1:
        if _printOutputs:
            print(subString + ' FOUND IN ' + inputString)
        return True
    else:
        if _printOutputs:
            print(subString + ' FOUND IN ' + inputString)
        return False

Main()