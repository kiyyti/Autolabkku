x = int(input())
for i in range(1, x+1):
    js = x - i
    ls = " " * js
    if i == 1:
        line_c = "*"
    elif i == x:
        line_c = "*" * (2 * i - 1)
    else:
        ninner = (2 * i) - 3
        inners = " " * ninner
        line_c = "*" + inners + "*"
    print(ls+line_c)