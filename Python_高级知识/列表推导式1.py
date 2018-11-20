#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     25/10/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    def t1():
        func1 = [lambda x: x*i for i in range(10)]
        result1 = [f1(2) for f1 in func1]
        #print result1
    def t2():
        func2 = [lambda x, i=i: x*i for i in range(10)]
        result2 = [f2(2) for f2 in func2]
        #print result2

    def t3():
        func3 = (lambda x: x*i for i in range(10))
        result3 = [f3(2) for f3 in func3]
        #print result3

    '''
    def t2():
        func2 = [lambda x, i=i: x*i for i in range(10)]
        #l=[print(i(0) for i in func2)]
        for i in func2:
            print(i(1))
        result2 = [f2(2) for f2 in func2]
        print(result2)
    '''
    t2()

if __name__ == '__main__':
    main()
