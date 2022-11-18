def backspace (a):
    a = list(a)
    c = '*'
    index_1 = len(a)-1 #Index elementov so zvezdochkami
    index_2 = len(a)-1 #Index elementov ostaln
    for x in range(len(a)-1):
        if a[index_1] == c:
            index_1 -= 1
    for x in range(len(a)-1):

        if a[index_2] != c:
            index_2 -= 1
        Delta = index_2-index_1
        del a[index_1 - Delta:index_2]#Kak dalshe zamknut ne ponimau
        index_2 = index_2 - Delta - 1
        index_1 = index_1 - Delta - 1
        return a, print(a)

backspace('**jkg*df**')

