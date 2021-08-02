fin = open("data.txt", "a")

def pack():
    usn = input("enter usn")
    name = input("enter name")
    sem = input("enter sem")
    dept = input("enter dept")
    data = f"{usn}|{name}|{sem}|{dept}|"
    fin.write(data)
    fin.write("\n")
    print("data added")
    fin.close()


def unpack():
    fout = open("data.txt", "r")
    data = fout.readlines()
    # print(data)
    for i in data:
        mystr = i.split("|")
        print(" ".join(mystr[0:4]))


def search(id):
    fout = open("data.txt", "r")
    data = fout.readlines()
    res = []
    # print(data)
    for i in range(len(data)):
        usn = data[i].split("|")
        res.append(usn[0])

    if id in res:
        tempid = res.index(id)
        output = []
        output = data[tempid].split("|")
        print(" ".join(output))
        return output, tempid
    else:
        print("data not found")
        return "Not Found"


def modify(usn):
    fout = open("data.txt", "r")
    data = fout.readlines()
    temp = search(usn)
    if temp == "Not Found":
        return
    sdata, index = temp
    print(sdata)

    sdata[0] = input("Enter new usn")
    sdata[1] = input("Enter new name")
    sdata[2] = input("Enter new sem")
    sdata[3] = input("Enter new branch")

    buff = sdata[0] + "|" + sdata[1] + "|" + sdata[2] + "|" + sdata[3] + "|"
    buff += "\n"
    data[index] = buff

    finput = open("data.txt", "w")
    for i in range(len(data)):
        finput.write(data[i])
    finput.close()
    fout.close()


def driver():

    while (True):
        ch = int(input("\nEnter your choice \n 1.Pack \n 2.Unpack \n 3.Search \n 4.Modify\n"))
        if (ch == 1):
            pack()
        elif ch == 2:
            unpack()
        elif ch == 3:
            usn = input("enter usn")
            search(usn)
        elif ch == 4:
            usn = input("enter usn")
            modify(usn)
        else:
            exit()


driver()
