import time
import zipModule
from datetime import datetime

sleepTime = 5
path = "C:\\Users\\felipe\\Desktop\\study\\python\\MultipleFiles\\project\\r_input"

def zip_file_listener(path):
    while True:
        zipFiles = zipModule.zipFiles(path)
        if not zipFiles:
            dt = datetime.now().strftime("%H:%M:%S")
            print('Could not find any zip file ' + dt) 
        else:
            for filePath in zipFiles:
                zipModule.unzip(filePath, path)
                zipModule.removeFile(filePath)
        
        time.sleep(sleepTime)
        print('Checking..')


def file_name_matches_with_interfaces(file_name, interfaces):
    if file_name in interfaces:
        return True
    return False


zip_file_listener(path)