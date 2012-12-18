p=[0.2, 0.2, 0.2, 0.2, 0.2]

world=['g', 'g', 'r', 'g', 'r']
measurements = ['r']
motions = [1]
pHit = 0.9
pMiss = 0.1
pExact = 1.0
pOvershoot = 0.0
pUndershoot = 0.0

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        if i - U < 0:
            s = 0.0
        else:
            s = pExact * p[(i-U)]
        if i + U > len(p) - 1:
            s += p[i]
        #s = s + pOvershoot * p[(i-U-1) % len(p)]
        #s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    #p = move(p, motions[k])
    
print p         

prob = 0.0
for i in range(len(p)):
    try:
        hit = ('r' == world[i + 1])
        prob += p[i] * (hit * pHit + (1 - hit) * pMiss)
    except IndexError:
        prob += p[i] * pHit
print prob
