fin = open("data.txt", "r")


def pack():
    data = fin.readlines()
    usn = input("Enter the usn:")
    name = input("Enter the Name:")
    sem = input("Enter the Sem:")
    dept = input("Enter the dept:")
    rrn = len(data)
    buf = f"{rrn+1}|{usn}|{name}|{sem}|{dept}"
    fout = open("data.txt", "a")
    fout.write(buf)
    fout.write("\n")
    print("Data added successfully")
    fout.close()
    fin.close()


def search():
    rrn = input("Enter the RRN")
    finput = open("data.txt","r")
    data = finput.readlines()
    temprrn = []
    for i in range(len(data)):
        temp = data[i].split("|")
        temprrn.append(temp[0])

    if rrn in temprrn:
        id = temprrn.index(rrn)
        mystr = data[id].split("|")
        print(" ".join(mystr))
    else:
        print("rrn not found")
    finput.close()

def driver():

    while True:
        ch = int(input("enter choice: 1.pack\n2.Search "))

        if ch == 1:
            pack()
        elif ch == 2:
            search()
        else:
            print("Wrong choice")
            exit()

driver()