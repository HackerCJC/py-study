#!/usr/bin/evn python3
# __*__ conding=utf-8 __*__

"""
"""
'''
    递归函数：
'''

if __name__ == '__main__':
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n - 1)


    print(fact(1))
    print(fact(5))
    print(fact(100))
    '''
        每次函数调用就会新增一层栈，函数返回较少一层栈，栈的大小是无限的，所以函数调用次数过多会造成栈溢出
        尾递归：类似for
    '''
    print(fact(1000))  # maximum recursion depth exceeded in comparison



    '''
        小结
            使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
            针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
            Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
    '''
