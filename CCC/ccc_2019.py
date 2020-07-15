def flip():
    x = input()
    m = [[1, 2], [3, 4]]
    for y in x:

        if y == "H":
            m[0], m[1] = m[1], m[0]
        elif y == "V":
            m[0][0], m[0][1] = m[0][1], m[0][0]
            m[1][0], m[1][1] = m[1][1], m[1][0]
    for i in m:
        for j in i:
            print(j, end=" ")
        print()
flip()