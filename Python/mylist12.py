myrows = int(input("Enter the number of rows: "))
k = 1
for i in range(0, myrows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()