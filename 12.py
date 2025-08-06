x = int(input("Input n: "))
if x < 10:
    for i in range(1,x+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
else:
    print("Program terminated!")