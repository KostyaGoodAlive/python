
def Sign(a,b):
    res = []
    res.append(a)
    res.append(b)
    while True:
     if b and a < 0:
         return -2
     elif b and a == 0:
        return 0
     elif a and b > 0 :
        return 2
     elif a < 0 and b > 0:
        return 0
     elif a > 0 and b < 0:
        return 0
     elif a < 0 :
        return -1
     elif b < 0 :
        return -1
     elif a > 0 :
        return 1
     elif b > 0 :
        return 1
     break
