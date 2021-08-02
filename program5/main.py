f1 = open("index.txt", "r")
f2 = open("data.txt", "r")


def sortdata():
    fout = open("index.txt", "w")
    fin = open("data.txt","r")
    details = fin.readlines()
    for i in range(len(details)):
        data = details[i].split("|")
        fout.write(f"{i}|{data[0]}|\n")
    fout.close()


def insert():
    name = input("enter name: ")
    usn = input("enter usn: ")
    sem = input("enter sem: ")
    branch = input("enter Branch: ")
    fout2 = open("data.txt", "a")
    buf = f"{usn}|{name}|{sem}|{branch}|\n"
    fout2.write(buf)
    fout2.close()
    print("data added successfully")
    sortdata()


def display():
    print("USN\tName\tSem\tBranch")
    details = f2.readlines()
    for i in range(len(details)):
        data = details[i].split("|")
        print("\t".join(data))


def search():
    usn = input("Enter the USN: ")
    lists = f1.readlines()
    f1.seek(0)
    id = 0
    flag = True
    for i in range(len(lists)):
        data = lists[i].split("|")
        if data[1] == usn:
            id = data[0]
            flag = False
            break
    if flag:
        print("Data not found")
        return
    f2.seek(0)
    sdata = f2.readlines()
    mystr = sdata[int(id)].split("|")
    print("USN\tName\tSem\tBranch")
    print("\t".join(mystr))


def delete():
    usn = input("Enter USN: ")
    indexing = open("index.txt", "r")
    stdata = open("data.txt", "r")
    lists = indexing.readlines()
    temp = stdata.readlines()
    for j in range(len(lists)):
        data = lists[j].split("|")
        if data[1] == usn:
            temp.pop(j)
    fouts = open("data.txt","w")
    for i in range(len(temp)):
        fouts.write(temp[i])
    fouts.close()
    sortdata()

def driver():
    while True:
        print("1.Insert\n2.Display\n3.Search\n4.Delete\n5.Exit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            insert()

        if choice == 2:
            display()

        if choice == 3:
            search()

        if choice == 4:
            delete()

        if choice == 5:
            print("Bye Bye f u  ")
            exit()


driver()
# sortdata()