while True:
    m, n = input().split(" ")
    m = int(m)
    n = int(n)

    if m <= 0 or n <= 0:
        break

    entre_numeros = []

    if m > n:
        while n <= m:
            entre_numeros.append(n)
            n += 1
    else:
        while m <= n:
            entre_numeros.append(m)
            m += 1

    soma = sum(entre_numeros)

    print(*entre_numeros, f'Sum={soma}')