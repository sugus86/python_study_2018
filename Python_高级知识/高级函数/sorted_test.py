
l=sorted([36, 5, 12, 9, 21])
print(l)


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

m=sorted([36, 5, 12, 9, 21], reversed_cmp)
print(m)

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

n=sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print(n)
