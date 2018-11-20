
print("*"*80)
try:
    import abc123
    print("try")
except:
    print("Exception")
else:
    print("else")

print("*"*80)
try:
    import abc123
    print("try")
except:
    print("Exception")
finally:
    print("finally")
print("*"*80)


#else:没有异常执行
#finally:有没有异常都执行
