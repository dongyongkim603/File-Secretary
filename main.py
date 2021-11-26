import os

class Main(object):

    success = False
    folder = None

    def load_folder(self, input_path):
        result = None
        if input_path is None:
            path = input("Enter the path of the folder: ")
            print(path)
        else:
            path = input_path
        try:
            result = os.listdir(path)
        except OSError:
            print("This is not a valid folder path")
        finally:
            return result

    def remove_duplicates(self):
        if self.folder is None:
            result = False
            print("There is no directory loaded currently")
        else:
            for file in self.folder:
                print(os.path.abspath(file))
            print("Duplicates removed")
            return True

    def menu(self):
        selection = None
        while selection is None:
            selection = input("Select action:\n(1) Load in directory"
                              "\n(2) Sort files by type\n(3) Remove duplicates\n(4) Exit program")
            print(selection)
            if selection == "1":
                self.load_folder()
            elif selection == "2":
                print("sorting files")
            elif selection == "3":
                self.remove_duplicates()
            elif selection == "4":
                self.success = True
            else:
                print("Invalid selection")

    def run(self):
        while not self.success:
            self.menu()
        print("Ending program... \nGoodbye...")


FS_file_secretary = Main()
FS_file_secretary.run()