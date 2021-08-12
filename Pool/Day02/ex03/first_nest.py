import sys
import os.path

class Research:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__final_list__ = []

    def check_file(self, has_header):
        if os.path.isfile(self.file_name) == False:
            print("Error: File does not exist")
            exit()
        file = open(self.file_name)
        if has_header == True:
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
            self.__final_list__.append([int(item) for item in (line.replace("\n", "")).split(",")])
        if flag == 0:
            file.close()
            raise Exception()
        file.close()

    def file_reader(self, has_header = True):
        try:
            self.check_file(has_header)
        except Exception:
            print("Error: Wrong format")
        else:
            return self.__final_list__

    class Calculations:
        def counts(self, data):
            count_of_head = 0
            count_of_tail = 0
            for i in data:
                count_of_head += i[0]
                count_of_tail += i[1]
            print(count_of_head, count_of_tail)

        def fractions(self):
            pass

if __name__=='__main__':
    my_obj = Research(sys.argv[1])
    data = my_obj.file_reader()
    print(my_obj.file_reader())
