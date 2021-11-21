class Research:
    def file_reader(self):
        try:
            file = open("../data.csv")
        except FileNotFoundError:
            return "Error: File not found"
        else:
            text = file.read()
            file.close()
            return text

def main():
    my_class = Research()
    print(my_class.file_reader())

if __name__=='__main__':
    main()