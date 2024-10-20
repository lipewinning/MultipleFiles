import os
from pathlib import Path
from datetime import datetime

def move_file(file_name, file_origin, file_destination):
    file_origin_path = file_origin + '\\' + file_name
    file_destination_path = file_destination + '\\' + file_name

    if os.path.isfile(file_origin_path):
        Path(file_origin_path).rename(file_destination_path + datetime.now().strftime("%H%M%S"))
    else:
        Path(file_origin_path).rename(file_origin_path)

def read_txt_file(file_path):
    if os.path.isfile(file_path):
        my_file = open(file_path, "r") 
        file_content_in_list = my_file.read().split("\n")
        my_file.close() 
        return file_content_in_list
    else:
        print('Could not find file ' + file_path)
        return None
    
def removeFile(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)
        print('REMOVE: ' + filePath)