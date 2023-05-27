n = int(input("Enter range: "))

for i in range(1, n + 1, 1):

    j = n
    for j in range(n, i, -1):
        print(end=" ")

    for k in range(1, i + 1, 1):
        if k == 1 or k == i:
            print(end="* ")
        else:
            print(end="  ")
    print()

for i in range(1, n + 1, 1):

    for j in range(1, i + 1, 1):
        print(end=" ")

    k = n
    for k in range(n, i, -1):
        if k == n or k == j:
            print(k, end=" ")
        else:
            print(end="  ")
    print()