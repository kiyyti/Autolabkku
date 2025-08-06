id12digit = input("")
if (len(id12digit) == 12 and id12digit.isdigit()):
    t_sum = 0
    for i in range(12):
        digit = int(id12digit[i])
        weight = 13 - i
        t_sum += digit * weight

    mod11 = t_sum % 11
    c_digit = (11 - mod11) % 10
    f_id = id12digit + str(c_digit)
    print(f"{f_id[0]} {f_id[1:5]} {f_id[5:10]} {f_id[10:12]} {f_id[12]}")