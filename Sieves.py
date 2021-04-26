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

