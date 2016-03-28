#!/usr/bin/env python3
# ! __*__ coding=utf-8 __*__
'python 高级特性之迭代: 列表生成器'
if __name__ == '__main__':
    '''
     类似于scala中的高级for循环之：for的推导式，使用yeild关键字返回新的可迭代对象,python中返回的是generator对象
     列表生成器中的下一个元素是通过计算得来，而不是一开始就直接创建好存放到内存当中
     比Java高级，java之中未见有这类功能
    '''
    print([x * x for x in range(10)])  # 使用列表生成式  打印一个列表
    print((x * x for x in range(10)))  # 使用列表生成器 打印一个generator对象 ,列表生成器对象可以通过不断调用next()方法获取下一个元素的值

    '案例：著名的斐波拉契数列（Fibonacci）'


    def fibonacci(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n += 1
        return 'done'


    print(fibonacci(6))

    '''
       若把 fibonacci 函数的 print 改为yeild 就是 fabonacci
    '''


    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b  # 调用next()方法时就是执行到yeild语句返回，再次调用从上次返回的yeild语句处开始执行
            a, b = b, a + b
            n += 1
        return 'done'


    fa = fib(6)
    # for x in fa:
    #     print('**', x)
    '''
        但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
        如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
    '''
    while True:
        try:
            x = next(fa)
            print('g:', x)
        except StopIteration as e:
            print('generate return value', e.value)
            break

    '''
        练习
         杨辉三角定义如下：
                   1
                1   1
              1   2   1
            1   3   3   1
          1   4   6   4   1
        1   5   10  10  5   1
    '''


    def triangles():
        # TODO 杨辉三角未实现
        pass


    '''
        小结
        generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
        要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
        对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
        请注意区分普通函数和generator函数，普通函数调用直接返回结果：
    '''
