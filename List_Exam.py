#John Patrick M. Salangsang CS - 201

listOdd = []
listEven = []

with open("Number.txt", "r+") as f:
    n10 = f.readline()
    n9 = f.readline()
    n8 = f.readline()
    n7 = f.readline()
    n6 = f.readline()
    n5 = f.readline()
    n4 = f.readline()
    n3 = f.readline()
    n2 = f.readline()
    n1 = f.readline()
f.close()

listOdd.append(int(n1))
listOdd.append(int(n3))
listOdd.append(int(n5))
listOdd.append(int(n7))
listOdd.append(int(n9))
listEven.append(int(n2))
listEven.append(int(n4))
listEven.append(int(n6))
listEven.append(int(n8))
listEven.append(int(n10))

sumOdd = sumEven = 0

with open("Salangsang_ODD_Prob1.txt", "w+") as f:
    f.write("Name: John Patrick Salangsang\n")
    for i in listOdd:
        f.write(f'{i} ')
        sumOdd += i
    f.write(f'\nSum: {sumOdd}\n')
    for i in listEven:
        f.write(f'{i} ')
        sumEven += i
        avg = sumEven // 5
    f.write(f'\nAverage: {avg}')
    f.write("\nName: John Patrick Salangsang")
f.close()
