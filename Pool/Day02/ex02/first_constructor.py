import sys
import os.path

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_file(self):
        if os.path.isfile(self.file_name) == False:
            print("Error: File does not exist")
            exit()
        file = open(self.file_name)
        header = file.readline()
        header_list = header.split(",")
        if len(header_list) != 2 or (header_list[0] == "" or header_list[1] == "\n"):
            raise Exception()
        flag = 0
        for line in file:
            flag = 1
            if line != '1,0\n' and line != '0,1\n' and line != '0,1' and line != '1,0':
                file.close()
                raise Exception()
        if flag == 0:
            file.close()
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