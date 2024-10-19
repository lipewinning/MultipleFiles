import shutil
import os
import glob

def unzip(inputFile,destinationFolder):
        shutil.unpack_archive(inputFile, destinationFolder,"zip")
        print('UNZIP: ' + inputFile)

def zipFiles(path):
    return glob.glob(path + '/*.zip')

def removeFile(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)
        print('REMOVE: ' + filePath)



