import random
import os


def renameAndCheck(file, dataFolder):
    pin = str(random.randint(1000, 999999))
    filename = file.filename
    newFilename =  pin + "-" + filename
    while os.path.exists(newFilename):
        pin = str(random.randint(1000, 999999))
        newFilename =  pin + "-" + filename
    file.save(dataFolder + newFilename)
    return pin, newFilename



def getDataByPin(pin, dataFolder):
    files = os.listdir(dataFolder)
    for file in files:
        if file.startswith(f"{pin}-"):
            fileStr = str(file)
            fileArr = fileStr.split("-")
            fileName = str(fileArr[-1])
            return fileName
    return None


