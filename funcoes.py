def multiprint(frase, x):
    for i in range(x):
        print(frase)


def isEven(n):
    if n % 2 == 0:
        print(f'O número {n} é par!')
        return True
    else:
        print(f'O número {n} é impar')
        return False
    
def sumandminus(x, y, z):
    res = x + y - z
    return res

from random import randint

n = randint(1, 10)
x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)

multiprint('Your turn to roll!', n)
isEven(n)
print(sumandminus(x, y, z))