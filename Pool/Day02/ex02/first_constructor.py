import sys
import os

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_file(self):
        try:
            file = open(self.file_name)
        except FileNotFoundError:
            print("Error: File not found")
            exit()
        else:
            header = file.readline()
            header_list = header.split(",")
            if len(header_list) != 2 or (header_list[0] == "" or header_list[1] == ""):
                raise Exception()
            for line in file:
                if line != "1,0" and line != "0,1":
                    raise Exception()
            file.close()

    def file_reader(self):
        try:
            self.check_file()
        except Exception:
            print("Error: Wrong format")
            exit()
        else:
            with open(self.file_name) as file:
                text = file.read()
            return text

if __name__=='__main__':
    my_obj = Research(sys.argv[1])
    print(my_obj.file_reader())