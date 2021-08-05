
def driver():

    list1 = input("Enter list1 delimited by #\n")
    list2 = input("Enter list2 delimited by #\n")

    list1File = open("list1.txt", "w")
    list1File.write(list1)

    list2File = open("list2.txt", "w")
    list2File.write(list2)

    list1File.close()
    list2File.close()

    list1Read = open("list1.txt", "r")
    list2Read = open("list2.txt", "r")

    temp1 = list1Read.readlines()
    temp1 = temp1[0].split("#")
    print(temp1)

    temp2 = list2Read.readlines()
    temp2 = temp2[0].split("#")
    print(temp2)

    # thirdList = ""
    # for i in range(len(temp1)):
    #     if temp1[i] in temp2:
    #         thirdList += temp1[i] + "#"
    #
    # list3 = open("list3.txt", "w")
    # list3.write(thirdList)
    #
    # temp3 = open("list3.txt", "r")
    #
    # temp3 = temp3.readlines()
    # temp3 = temp3[0].split()
    # print(temp3)



driver()
