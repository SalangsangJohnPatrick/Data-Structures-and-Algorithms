##JOHN PATRICK M. SALANGSANG
##KEENO C. CRUZ
##CS - 201

array = []

def shellAsc(array, n):
    interval = n
    print("List of Comparison:")
    for i in range(5):
        if i >= n:
            i += n
            if interval % 2 == 0 and interval <= 10:
                interval += n
        temp = array[i]
        j = i
        if interval >= 10:
            break
        print(temp, ">", array[interval])
        if j <= n and temp > array[interval]:
            array[j], array[interval] = array[interval], temp
        interval += 1

def shellDesc(descArray, n):
    interval = n
    print("List of Comparison:")
    for i in range(5):
        if i >= n:
            i += n
            if interval % 2 == 0 and interval <= 10:
                interval += n
        temp = descArray[i]
        j = i
        if interval >= 10:
            break
        print(temp, "<", descArray[interval])
        if j <= n and temp < descArray[interval]:
            descArray[j], descArray[interval] = descArray[interval], temp
        interval += 1

def insertionAsc(array):
    for i in range(0, len(array)):
        print('Loop', i)
        for k in array:
            print("\t", k, end=" ")
        print()
        for j in range(0, i):
            temp = array[i]
            j = i - 1
                
            while (j >= 0 and temp < array[j]):
                array[j + 1] = array[j]
                j = j - 1
                array[j + 1] = temp
                    
                for k in array:
                    print("\t", k, end=" ")
                print()

def insertionDesc(descArray):
    for i in range(0, len(descArray)):
        print('Loop', i)
        for k in descArray:
            print("\t", k, end=" ")
        print()
        for j in range(0, i):
            temp = descArray[i]
            j = i - 1
                
            while (j >= 0 and temp > descArray[j]):
                descArray[j + 1] = descArray[j]
                j = j - 1
                descArray[j + 1] = temp
                    
                for k in descArray:
                    print("\t", k, end=" ")
                print()

def menu():
    descArray = array.copy()
    option = input("Order:\n\
[a] Ascending\n\
[b] Descending\n\
[c] Exit\n\
Enter choice: ")
    
    if option == 'a':
        shellAsc(array, interval)
        print("Partial Order:", *array)
        print("Insertion Process:")
        insertionAsc(array)
        print()
        menu()
    
    elif option == 'b':
        shellDesc(descArray, interval)
        print("Partial Order:", *descArray)
        print("Insertion Process:")
        insertionDesc(descArray)
        print()
        menu()

    elif option == 'c':
        print("System terminated.")

    else:
        print("Invalid.")
        print()
        menu()

while len(array) < 10:
    try:
        num = int(input("Input a number " + str(len(array) + 1) + ": "))
        if num in array:
            print("The number already exists.")
        else:
            array.append(num)
    except ValueError:
        print("Input only numerical value.")
        continue
    
while True:
    interval = int(input("Interval value: "))
    try:
        if interval <= 1:
            print("Invalid interval.")
        else:
            break
    except ValueError:
        print("Input only numerical value.")
menu()
    

    
