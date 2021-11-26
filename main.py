import os

class Main:

    def load_folder(input_path):
        if input_path is None:
            path = input("Enter the path of the folder: ")
            print(path)
        else:
            path = input_path
        try:
            file_array = os.listdir(path)
            for file in file_array:
                if os.path.isfile(path + "\\" + file):
                    print("FILE: " + file)
                else:
                    print("FOLDER: " + file)
        except OSError:
            print("This is not a valid folder path")
        finally:
            print("Ending file read")

    load_folder(None)
