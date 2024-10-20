import os

def move_file(file_name, file_origin, file_destination):
    return True

def read_txt_file(file_path):
    if os.path.isfile(file_path):
        my_file = open(file_path, "r") 
        file_content_in_list = my_file.read().split("\n")
        my_file.close() 
        return file_content_in_list
    else:
        print('Could not find file ' + file_path)
        return None