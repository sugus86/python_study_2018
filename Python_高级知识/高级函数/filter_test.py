
def is_odd(n):
    return n % 2 == 1

l=filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print(list(l))


def not_empty(s):
    return s and s.strip()

m=filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print(list(m))
