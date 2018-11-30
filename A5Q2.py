def sumListPos_rec(a,l):
    if len(a) == 0:
        return 0
    else:
        if a[0] > 0:
            return a[0] + sumListPos_rec(a[1:],l)
        else:
            return 0 + sumListPos_rec(a[1:],l)
