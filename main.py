import os


def load_folder():
    path = input("Enter the path of the folder: ")
    print(path)
    file_array = os.listdir(path)
    

load_folder()