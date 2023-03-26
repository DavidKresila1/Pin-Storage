import random
import os


def renameAndCheck(file, dataFolder):
    pin = str(random.randint(1000, 999999))
    filename = file.filename
    newFilename = dataFolder + pin + "-" + filename
    while os.path.exists(newFilename):
        pin = str(random.randint(1000, 999999))
        newFilename = dataFolder + pin + "-" + filename
    file.save(newFilename)
    return pin, newFilename



def getDataByPin(pin, dataFolder):
    files = os.listdir(dataFolder)
    for file in files:
        if file.startswith(f"{pin}-"):
            title = file
            return os.path.join(dataFolder, file)
    return None


