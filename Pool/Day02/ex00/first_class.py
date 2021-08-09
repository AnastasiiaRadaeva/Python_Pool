class Must_read:
    try:
        file = open("../data.csv")
    except FileNotFoundError:
        print("Error: File not found")
    else:
        print(file.read())
        file.close()

if __name__=='__main__':
    Must_read