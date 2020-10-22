def buyandsell(A,n):
    i=0

    if len(A) < 2:
        return 0
    minp = A[0]
    p = 0
    for a in A[1:]:
        p = max(p, a - minp)
        minp = min(minp, a)
    return p






price = [10,11,14,16,34,23,12,34,35,24,25,100]
n = len(price)
print(buyandsell(price,n))
