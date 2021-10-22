def RootsOf(a, b, c):
    x0 = (-b - ((b**2)-(4*a*c))**0.5) / (2*a)
    x1 = (-b + ((b**2)-(4*a*c))**0.5) / (2*a)
    return x0, x1
