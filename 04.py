x = input("")
if (len(x) == 12 and x.isdigit()):
    n = 0
    for i in range(12):
        digit = int(x[i])
        weight = 13 - i
        n += digit * weight

    n12 = (11 - (n % 11)) % 10
    print(f"{x[0]} {x[1:5]} {x[5:10]} {x[10:12]} {x[12]} {n12}")