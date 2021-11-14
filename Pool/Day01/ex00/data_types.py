def data_types():
    my_int = 7
    my_str = "hello"
    my_float = 7.9
    my_bool = True
    my_list = [1, 2, 3, 4, 5]
    my_dict = {'a':1, 'b':2}
    my_tuple = (1, 2, 3, 4, 5)
    my_set = {"a", "b"}
    my_list = [type(my_int).__name__, type(my_str).__name__, type(my_float).__name__,
               type(my_bool).__name__, type(my_list).__name__, type(my_dict).__name__,
               type(my_tuple).__name__, type(my_set).__name__]
    final_list = ["[", ', '.join(my_list), "]"]
    print(*final_list, sep="")

if __name__=='__main__':
    data_types()