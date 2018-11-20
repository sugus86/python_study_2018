#同一个代码块的语句必须包含相同的缩进空格数

if True:
    print ("Answer")
    print ("True")
else:
  print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误
