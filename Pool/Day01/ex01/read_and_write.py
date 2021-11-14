def process_line(line):
    new_line = list(line)
    flag = 0
    for i in range(len(new_line)):
        if new_line[i] == "\"":
            flag += 1
        if new_line[i] == "," and flag % 2 == 0:
            new_line[i] = "\t"
    return "".join(new_line)

def process_file(file_name):
    file = open(file_name)
    new_file = open("./ds.tsv", 'w')
    for line in file:
        new_file.write(process_line(line))
    file.close()
    new_file.close()

if __name__=='__main__':
    process_file("./ds.csv")