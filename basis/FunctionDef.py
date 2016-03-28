#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
if __name__ == '__main__':
    '''
        1、调用函数：python内置许多函数，可以直接调用
    '''
    print(abs(-200))  # 求绝对值
    # print(abs(1, 2)) TypeError: abs() takes exactly one argument (2 given)
    # print(abs('a')) TypeError: bad operand type for abs(): 'str'

    '''
        python内置函数：数据类型转换函数
    '''

    print(int('123'))
    print(int(12.34))
    print(float('12.34'))
    print(str(12.34))
    print(bool(1))  # True
    print(bool(''))  # False
    print(bool(0))  # False
    print(bool([]))  # False

    '''
        形同scala
        函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
    '''
    a = abs  # 变量a指向abs函数
    print(a(-90))  # 所以也可以通过a调用abs函数

    '''
        练习
        请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
    '''
    n1 = 255
    n2 = 1000
    print(str(hex(n1)))

    '''
        小结
        调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！
    '''

    '''
        2、定义函数：
        在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
        ，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

         def myAbs(x):
        if x > 0:
            return x
        else:
            return -x


    print(myAbs(-10))
    '''

    '''
        如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
        return None可以简写为return。
    '''


    def f1():
        return


    print(f1())  # none

    from basis.FunUtil import myAbs  # 引入外部文件中自己定义的函数 from后面跟文件名没有.py后缀, import 后面跟函数名

    print(myAbs(-90))

    '''
        如果想定义一个什么也不做的空函数可以使用pass
        pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
        pass还可以用在其他语句里，比如：
        缺少了pass，代码运行就会有语法错误
if age >= 18:
    pass
    '''


    def nop():
        pass


    '''
        调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
    '''
    # print(myAbs(1, 2))  # TypeError: myAbs() takes 1 positional argument but 2 were given

    '''
        返回多个值
        函数可以返回多个值吗？答案是肯定的。
        比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
    '''
    import math


    def move(xx, yy, step, angle=0):
        nx = xx + step * math.cos(angle)
        ny = yy - step * math.sin(angle)
        return nx, ny


    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)
    '''
        但其实这只是一种假象，Python函数返回的仍然是单一值：其实返回的就是一个tuple,可以省略括号 按照位置用变量获取返回值
    '''
    r = move(100, 100, 60, math.pi / 6)
    print(r)

    '''
        小结:
            定义函数时，需要确定函数名和参数个数；
            如果有必要，可以先对参数的数据类型做检查；
            函数体内部可以用return随时返回函数结果；
            函数执行完毕也没有return语句时，自动return None。
            函数可以同时返回多个值，但其实就是一个tuple。
    '''

    '''
        练习
            请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
            ax2 + bx + c = 0
            的两个解。
            提示：计算平方根可以调用math.sqrt()函数：
    '''
    def quadratic(a, b, c):
        pass