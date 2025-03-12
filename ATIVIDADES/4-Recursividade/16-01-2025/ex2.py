def pot(n1, n2):
    if n2 == 0:
        return 1
    else:
        return n1 * pot(n1, n2-1)

print(pot(2,3))
