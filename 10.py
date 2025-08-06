result = input()
top = input()

if len(top) != len(result):
    print("Incomplete answer")
else:
    x = 0
    for i in range(len(result)):
        if top[i] == result[i]:
            x += 1
    print(x)  