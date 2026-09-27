import time

LIMITE = 1000000

def generar_primos_base(max_val):
    base = [2]
    for n in range(3, max_val + 1, 2):
        es_p = True
        raiz = int(n**0.5)
        for p in base:
            if p > raiz:
                break
            if n % p == 0:
                es_p = False
                break
        if es_p:
            base.append(n)
    return base

def esprimo(n, primos_base):
    limite = int(n**0.5)
    for p in primos_base:
        if p > limite:
            break
        if n % p == 0:
            return False
    return True


def prog():
    t1 = time.time()
    primos_base = generar_primos_base(int(LIMITE**0.5) + 1)

    for i in range(11, LIMITE, 10):
        if esprimo(i, primos_base) and esprimo(i+2, primos_base) and esprimo(i+6, primos_base) and esprimo(i+8, primos_base):
            print(i, i+2, i+6, i+8)
            
    t2 = time.time()
    print(t2 - t1)

prog()
