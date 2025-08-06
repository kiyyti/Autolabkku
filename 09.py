x = 0
n = []
while 1:
    x = input()
    if len(n) == 0 and x == "q":
        print("No Data")
        break
    elif x == "q":
        print(round(sum(n)/len(n),2))
        break
    else:
        n.append(float(x))
