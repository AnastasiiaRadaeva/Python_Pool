def data_types():
    my_list = [type(int()).__name__, type(str()).__name__, type(float()).__name__,
               type(bool()).__name__, type(list()).__name__, type(dict()).__name__,
               type(tuple()).__name__, type(set()).__name__]
    print(my_list)

if __name__=='__main__':
    data_types()