input = [1, 2, 3, 4, 5, 6, 12, 87, 21]
t = [0] * (3 * len(input)) + input
"""
t[i] = v
x - current node
lx, lx - left and right bound of sequences of element which consist in x node
"""
def set(i, v, x, lx, rx): 
    if rx - lx == 1:
        t[x] = v
        return 
    m = (lx + rx) // 2
    if i < m:
        set(i, v, 2*x + 1, lx, m)
    else:
        set(i, v, 2*x + 2, m, rx)
    t[x] = t[2*x + 1] + t[2*x + 2]
     
def sum(l, r, x, lx, rx):
    if lx >= r or rx <= l:
        return 0
    if lx >= l and rx <= r:
        return t[x]
    mid = (lx + rx) // 2
    sum_l = sum(l, r, 2*x + 1, lx, mid)
    sum_r = sum(l, r, 2*x + 2, mid, rx)
    return sum_l + sum_r

def build(a, t, x, lx, rx):
    if rx - lx == 1:
        t[x] = a[lx]
        return
    m = (lx + rx) // 2
    build(a, t, 2*x + 1, lx, m)
    build(a, t, 2*x + 2, m, rx)
    t[x] = t[2*x + 1] + t[2*x + 2]

build(input, t, 0, 0, len(input))

print(sum(2, 4, 0, 0, len(input)))  # should print 12
