def combine(n,m):
    q = ''
    for i in range(len(n)):
        q += n[i] + m[i]
    return q

def disconnection(q):
    n = q[::2]
    m = q[1::2]
    return n,m