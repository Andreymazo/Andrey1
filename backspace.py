def backspace (a):
    a = list(a)
    c = '*'
    index_1 = 0 #Index elementov so zvezdochkami
    index_2 = 0 #Index elementov ostaln
    for x in a:
        if x == c and inddex_2 == 0:
            a = a[index_1 + 1]
        elif x == c and index_2 != 0:
            a = a[:index_1-1] + [index_2+1:]
            index_1 -= 1
            index_2 -= 1
        elif x == c and index_1 == len(a)-1:
            a=a[:index_1-1]
        elif x != c:
            index_2 += 1
            index_1 += 1

        return a,print(a)

backspace('**jkg*df**')

