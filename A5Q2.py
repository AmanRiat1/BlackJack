#a
def stars(n):    
    if n == 0:
        return 
    print("*"*n)
    stars(n-1)
    print("*"*n)

#b
def sumListPos_rec(a,l):
    d = a[:l]
    if len(d) == 0:
        return 0
    else:
        if d[0] > 0:
            return d[0] + sumListPos_rec(d[1:],l)
        else:
            return 0 + sumListPos_rec(d[1:],l)
