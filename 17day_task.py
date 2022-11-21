def solve(n, repeats):
    c = ""
    n = str(n)
    Total = []
    for i in range(repeats):

        c = c + c.join(n)
        Total.append(c)

        Total = [int(x) for x in Total]


        print(sum(Total))

solve(5, 3)  # 615

