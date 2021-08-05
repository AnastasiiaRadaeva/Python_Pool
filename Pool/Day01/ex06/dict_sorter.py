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
    new_dict = {k: v for k, v in list_of_tuples}
    sorted_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[0])}
    sorted_dict_final = {k: v for k, v in sorted(sorted_dict.items(), key=lambda item: int(item[1]), reverse=True)}
    for k, v in sorted_dict_final.items():
        print(k, v)

if __name__=='__main__':
    make_dict()