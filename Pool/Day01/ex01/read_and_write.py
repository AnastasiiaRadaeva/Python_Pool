

def process_line(line):
    new_line = line.replace(", ", "(;")
    list_of_line = new_line.split(',')
    return "\t".join(list_of_line)

def process_file(file_name):
    file = open(file_name)
    new_file = open("./ds.tsv", 'w')
    for line in file:
        new_line = process_line(line)
        new_file.write(new_line.replace("(;", ", "))

if __name__=='__main__':
    process_file("./ds.csv")