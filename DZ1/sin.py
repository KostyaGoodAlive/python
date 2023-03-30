
def Sign(x):
     if x < 0:
         return -1
     elif x == 0:
        return 0
     elif x > 0 :
        return 1

if __name__ == '__main__':
    print('Sign.py module started')
    print(Sign(-4))

