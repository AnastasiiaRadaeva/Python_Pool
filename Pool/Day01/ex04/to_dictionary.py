def print_dict(dict_for_print):
    for k, v in dict_for_print.items():
        if type(v) == list:
            for i in v:
                print("'" + k + "'", ":", end="")
                print(" '"+i+"'")
        else:
            print("'"+k+"'", ":", "'"+v+"'")

def make_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    new_dict = {}
    for i in list_of_tuples:
        if i[1] in new_dict:
            tmp_list = [new_dict.get(i[1])]
            tmp_list.append(i[0])
            new_dict[i[1]] = tmp_list
        else:
            new_dict[i[1]] = i[0]
    print_dict(new_dict)
if __name__=='__main__':
    make_dict()