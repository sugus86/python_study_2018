def unique_pairs(n):
    """在 range(n) 范围内生成索引对"""
    for i in range(n):
        for j in range(i+1, n):
            yield i, j

s = "a string to examine"
for i, j in unique_pairs(len(s)):
    print(i,j)
    '''
    if s[i] == s[j]:
        answer = (i, j)
        #print(answer)
        break
    '''
