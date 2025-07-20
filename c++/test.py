def DrawLine(P0, P1, color):
    x0 = P0[0]
    x1 = P1[0]
    y0 = P0[1]
    y1 = P1[1]
    a = (y1 - y0) / (x1 - x0)
    b = y0 - a * x0
    for x in range(x0, x1):
        y = a * x + b
        print(x, y, color)


DrawLine([10, 20], [50, 15], 'red')
