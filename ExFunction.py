def ExFunction(x, N):

    t, f, i = 1, 1, 1

    while (N+1 != i):
        f = f*i
        t = t+(x**i)/f
        i += 1

    return t


print(ExFunction(3, 3))
