class Must_read:
    file = open("./data.csv")
    for line in file:
        print(line, end="")
    print("")
if __name__=='__main__':
    Must_read