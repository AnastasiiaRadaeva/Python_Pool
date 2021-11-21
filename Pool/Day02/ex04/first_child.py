import sys
from random import randint


class Research:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__final_list__ = []

    def check_file(self, has_header):
        with open(self.file_name) as f:
            lines = f.readlines()
        if (has_header is True and len(lines) < 2) or (has_header is False and len(lines) < 1):
            raise Exception()
        if has_header:
            header = lines[0]
            header_list = header.split(",")
            if len(header_list) != 2 or (header_list[0] == "" or header_list[1] == "\n"):
                raise Exception()
            lines.pop(0)
        for line in lines:
            if line != '1,0\n' and line != '0,1\n' and line != '0,1' and line != '1,0':
                raise Exception()
            self.__final_list__.append([int(item) for item in (line.replace("\n", "")).split(",")])

    def file_reader(self, has_header=True):
        self.__final_list__ = []
        try:
            self.check_file(has_header)
        except Exception:
            print("Error: Wrong format or file can not be read")
            exit()
        else:
            return self.__final_list__

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0
            for i in self.data:
                heads += i[0]
                tails += i[1]
            return [heads, tails]

        def fractions(self, heads, tails):
            h = float(heads) / float((heads + tails)) * 100
            t = float(tails) / float((heads + tails)) * 100
            return [h, t]

    class Analytics(Calculations):
        def predict_random(self, number_of_pred):
            my_list = []
            for i in range(number_of_pred):
                rand_num = 1 - randint(0, 1)
                my_list.append([rand_num, 1 - rand_num])
            return my_list

        def predict_last(self):
            return self.data[-1]

def main():
    if len(sys.argv) != 2:
        raise RuntimeError('Wrong number of arguments')
    obj = Research(sys.argv[1])
    my_list = obj.file_reader()
    print(my_list)
    calc = obj.Calculations(my_list)
    h_t = calc.counts()
    for i in h_t:
        # print(i, end=" ")
        print(i)
    print("\n")
    h_t = calc.fractions(h_t[0], h_t[1])
    for i in h_t:
        # print(i, end=" ")
        print(i)
    print("\n")
    anltc = obj.Analytics(my_list)
    print(anltc.predict_random(3))
    print(anltc.predict_last())

if __name__=='__main__':
    main()