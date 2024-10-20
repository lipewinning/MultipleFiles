import time
import zipModule
import fileModule
from datetime import datetime
import re
import os

sleepTime = 5
path = "C:\\Users\\felipe\\Desktop\\study\\python\\MultipleFiles\\project\\r_input"
interface_file_path = "C:\\Users\\felipe\\Desktop\\study\\python\\MultipleFiles\\project\\r_config_interface\\interfaces.txt"

def interface_listener(path, interface_list):
    interface_list = fileModule.read_txt_file(interface_file_path)
    while True:
        print('\n -->> Checking directory ' + path)  
        zipFiles = zipModule.zipFiles(path)
        if not zipFiles:
            dt = datetime.now().strftime("%H:%M:%S")
            print('     Could not find any zip file ' + dt) 
        else:
            for filePath in zipFiles:
                if is_it_a_registered_interface(filePath, interface_list):
                    zipModule.unzip(filePath, path)
                    zipModule.removeFile(filePath)
                else:
                    print('Error not registered file ' + filePath)
        
        time.sleep(sleepTime)
        


def is_it_a_registered_interface(file_path, interfaces):
    file_name = os.path.basename(file_path).split('/')[-1].split('_')[0]

    if file_name in interfaces:
        return True
    return False


interface_list = fileModule.read_txt_file(interface_file_path)
if interface_list is None:
    print('ERROR: Check the interfaces in ' + interface_file_path)
else:
    interface_listener(path, interface_list)