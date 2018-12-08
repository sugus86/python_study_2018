import random
def gen_random_list(opts, n):  
    return [random.choice(opts) for i in range(n)]

print(gen_random_list('123456', 5))