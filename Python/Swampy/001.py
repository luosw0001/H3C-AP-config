__author__ = 'TIW'



def cisco(n):
    if n == 0:
        return 1
    else:
        a = cisco(n-1)
        b = n * a
        return b

def k(n):
    print(cisco(n))



k(10)


def huawei(n):
    while n >= 0:
        if  n == 0:
            return 1
        else:
            a = huawei(n-1)
            b = n * a
            return b
            print(b)
    print("Shit!")

print(huawei(10.5))
