##JOHN PATRICK M. SALANGSANG
##KEENO C. CRUZ
##CS - 201

numbers = []
temp = 0
_min = 0

while len(numbers) < 6:
    num = int(input('Enter 6 items: '))
    if num in numbers:
        print('The number already exists.')
    else:
        numbers.append(num)
print()

def bubbleSort():
    print("Sort elements in:\n[1] Ascending\n[2] Descending")
    order = int(input("Enter Option: "))
    for k in numbers:
        print("\t", k, end=" ")
    print()
    if order == 1:
        for i in range(0, len(numbers)):
            print("Loop ", i)
            for j in range(0, len(numbers)-1):
                if numbers[j] > numbers[j+1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j+1]
                    numbers[j+1] = temp
                for k in numbers:
                    print("\t", k, end=" ")
                print()
    elif order == 2:
        for i in range(0, len(numbers)):
            print("Loop ", i)
            for j in range(0, len(numbers)-1):
                if numbers[j] < numbers[j+1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j+1]
                    numbers[j+1] = temp
                for k in numbers:
                    print("\t", k, end=" ")
                print()
    else:
        print('Invalid.')

def selectionSort():
    print("Sort elements in:\n[1] Ascending\n[2] Descending")
    order = int(input("Enter Option: "))
    for k in numbers:
        print("\t", k, end=" ")
    print()
    if order == 1:
        for i in range(0, len(numbers)):
            _min = i
            for j in range(i+1, len(numbers)):
                if numbers[_min] > numbers[j]:
                    temp = numbers[j]
                    numbers[j] = numbers[_min]
                    numbers[_min] = temp
            print('Loop', i)
            for k in numbers:
                print("\t", k, end=" ")
            print()
    elif order == 2:
        for i in range(0, len(numbers)):
            _min = i
            for j in range(i+1, len(numbers)):
                if numbers[_min] < numbers[j]:
                    temp = numbers[j]
                    numbers[j] = numbers[_min]
                    numbers[_min] = temp
            print('Loop', i)
            for k in numbers:
                print("\t", k, end=" ")
            print()
    else:
        print('Invalid.')

def insertionSort():
    print("Sort elements in:\n[1] Ascending\n[2] Descending")
    order = int(input("Enter Option: "))
    if order == 1:
        for i in range(0, len(numbers)):
            print('Loop', i)
            for k in numbers:
                print("\t", k, end=" ")
            print()
            for j in range(0, i):
                temp = numbers[i]
                j = i - 1
                
                while (j >= 0 and temp < numbers[j]):
                    numbers[j + 1] = numbers[j]
                    j = j - 1
                    numbers[j + 1] = temp
                    
                    for k in numbers:
                        print("\t", k, end=" ")
                    print()
    elif order == 2:
        for i in range(0, len(numbers)):
            print('Loop', i)
            for k in numbers:
                print("\t", k, end=" ")
            print()
            for j in range(0, i):
                temp = numbers[i]
                j = i - 1
                
                while (j >= 0 and temp > numbers[j]):
                    numbers[j + 1] = numbers[j]
                    j = j - 1
                    numbers[j + 1] = temp
                    
                    for k in numbers:
                        print("\t", k, end=" ")
                    print()
    else:
        print('Invalid.')

def options():
    print("Sorting Process:\n[1] Bubble Sort\n[2] Selection Sort\n[3] Insertion Sort\n[4] Exit")
    try:
        choose = int(input("Enter Option: "))
        print()
    except ValueError:
        print("Only enter numeric value.")
        print()
        options()
    else:
        if choose == 1:
            bubbleSort()
            print()
            options()
        elif choose == 2:
            selectionSort()
            print()
            options()
        elif choose == 3:
            insertionSort()
            print()
            options()
        elif choose == 4:
            print("System Exit.")
        else:
            print("Invalid. Try again.")
            options()
options()
