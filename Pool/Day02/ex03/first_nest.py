import sys
import os.path


class Research:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__final_list__ = []
        self.calc = self.Calculations()

    def check_file(self, has_header):
        if not os.path.isfile(self.file_name):
            print("Error: File does not exist")
            exit()
        file = open(self.file_name)
        if has_header:
            header = file.readline()
            header_list = header.split(",")
            if len(header_list) != 2 or (header_list[0] == "" or header_list[1] == "\n"):
                file.close()
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

    def file_reader(self, has_header=True):
        self.__final_list__ = []
        try:
            self.check_file(has_header)
        except Exception:
            print("Error: Wrong format")
            exit()
        else:
            return self.__final_list__

    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for i in data:
                heads += i[0]
                tails += i[1]
            return [heads, tails]

        def fractions(self, heads, tails):
            h = float(heads) / float((heads + tails)) * 100
            t = float(tails) / float((heads + tails)) * 100
            return [h, t]


def main():
    if len(sys.argv) != 2:
        raise RuntimeError('Wrong number of arguments')
    my_obj = Research(sys.argv[1])
    my_calc = my_obj.calc
    my_list = my_obj.file_reader()
    print(my_list)
    h_t = my_calc.counts(my_list)
    for i in h_t:
        print(i, end=" ")
    print("\n")
    h_t = my_calc.fractions(h_t[0], h_t[1])
    for i in h_t:
        print(i, end=" ")
    print("\n")


if __name__ == '__main__':
    main()
