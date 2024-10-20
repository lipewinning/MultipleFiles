import shutil
import os
import glob

fileExtension = "zip"

def unzip(inputFile,destinationFolder):
        shutil.unpack_archive(inputFile, destinationFolder, fileExtension)
        print('UNZIP: ' + inputFile)

def zipFiles(path):
    return glob.glob(path + '/*.' + fileExtension)

def removeFile(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)
        print('REMOVE: ' + filePath)



