num = int(input("Input number of groups: "))

if 5 <= num <= 21 :
    for i in range(1,num+1):
        print("Group", str(i) + ":", end=" ")
        for j in range(i, 101, num):
            print(str(j), end=" ")
        print()
else:
    print("Out of range! Program terminated")