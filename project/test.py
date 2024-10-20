import re
import fileModule
interface_file_path = "C:\\Users\\felipe\\Desktop\\study\\python\\MultipleFiles\\project\\r_config_interface\\interfaces.txt"
import os

file_path = "C:\\Users\\felipe\\Desktop\\study\\python\\MultipleFiles\\project\\r_config_interface\\BR02_20240205.txt"

def is_it_a_registered_interface(file_path, interfaces):
    file_name = os.path.basename(file_path).split('/')[-1].split('_')[0]

    if file_name in interfaces:
        return True
    return False

interface_list = fileModule.read_txt_file(interface_file_path)
print(is_it_a_registered_interface(file_path, interface_list))