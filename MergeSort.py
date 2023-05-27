##JOHN PATRICK M. SALANGSANG
##CS - 201

merge = []
print("Input 8 numbers:")

def mergeSort(merge):
    if len(merge) > 1:
        mid = len(merge) // 2
        leftHalf = merge[:mid]
        rightHalf = merge[mid:]

        print("Sublist: ", leftHalf)
        print("Sublist: ", rightHalf)

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                merge[k] = leftHalf[i]
                i = i + 1
            else:
                merge[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            merge[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            merge[k] = rightHalf[j]
            j = j + 1
            k = k + 1
        print("Merge: ", merge)

def mergeSort2(merge2):
    if len(merge2) > 1:
        mid = len(merge2) // 2
        leftHalf = merge2[:mid]
        rightHalf = merge2[mid:]

        print("Sublist: ", leftHalf)
        print("Sublist: ", rightHalf)

        mergeSort2(leftHalf)
        mergeSort2(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] > rightHalf[j]:
                merge2[k] = leftHalf[i]
                i = i + 1
            else:
                merge2[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            merge2[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            merge2[k] = rightHalf[j]
            j = j + 1
            k = k + 1
        print("Merge: ", merge2)
        
def menu():
    while len(merge) < 8:
        num = int(input("Number " + str(len(merge) + 1) + ": "))
        if num in merge:
            print("The number is already in list.")
        else:
            merge.append(num)
    print()
    merge2 = merge.copy()
    print("Order:\n[a] ASCENDING\n[b] DESCENDING\n[c] EXIT")
    option = input("Enter option: ").lower()
    if option == 'a':
        mergeSort(merge)
        menu()
    elif option == 'b':
        mergeSort2(merge2)
        menu()
    elif option == 'c':
        print("Exit")
    elif option.isdigit():
        print("Only enter an alphabetical character. Try again.")
        menu()
    else:
        print("Invalid. Try again.")
        menu()
menu()
