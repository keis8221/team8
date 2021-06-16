def prime(n):
    l = list(range(2, n+1))
    i = 0
    while i < len(l):
        l = [j for j in l if not(j%l[i] == 0) or (j/l[i] == 1)]
        i+= 1
    else:
        return l

print(prime(20))