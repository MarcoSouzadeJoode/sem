import numpy as np
from collections import deque

def eratosthenes(n):
    multiples = []
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return np.array(primes)

def eratosthenes_boolean(n):
    L = np.ones((n,), dtype="bool")
    for i in range(2,n):
        k = 2
        while k*i < n:
            L[k*i] = False
            k += 1
    L[0], L[1] = False, False
    return np.array([i for i, l in enumerate(L) if l])


def eratosthenes_optimized(n):
    primes = [i for i in range(2,n+1)]
    for i in primes:
        k = 2
        while k*i <= n:
            try:
                primes.remove(k*i)
            except ValueError:
                pass
            k+= 1
    return primes

def sundaram_naive_boolean(n):
    m = n//2
    L = [True] * n
    
    for i in range(1, m):
        L[2*i] = False
        for j in range(1, m):
            U = i + j + 2*i*j
            if U < m:
                L[2*U+1] = False

    L[0], L[1], L[2] = False, False, True
    return np.array([i for i, l in enumerate(L) if l])

def sundaram_naive_set(n):
    m = n // 2
    L = {l for l in range(1,m)}
    for i in range(1,m):
        for j in range(i,m):
            U = i + j + 2*i*j
            if U < m:
                L.discard(U)
    primes = deque([2*l+1 for l in L])
    primes.extendleft([2])
    return np.array(primes)


def sundaram_optimized_set(n):
    m = n // 2
    L = {l for l in range(1,m)}
    for i in range(1,m):
        limit = (m-i)//(2*i+1)
        for j in range(i, limit+1):
            U = i + j + 2*i*j
            L.discard(U)
    primes = deque([2*l+1 for l in L])
    primes.extendleft([2])
    return np.array(primes)


def sundaram_optimized_boolean(n):
    m = n//2
    L = [True] * n
    
    for i in range(1, m):
        L[2*i] = False
        limit = (m-i)//(2*i+1)
        for j in range(i, limit+1):
            U = i + j + 2*i*j
            if U < m:
                L[2*U+1] = False

    L[0], L[1], L[2] = False, False, True
    return np.array([i for i, l in enumerate(L) if l])

