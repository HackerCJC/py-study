#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
'''
"""
    Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
    还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，
    不但能处理复杂的参数，还可以简化调用者的代码。
"""
if __name__ == '__main__':
    '''
        位置参数
    '''


    def power(x):
        return x * x


    '''
    对于power(x)函数，参数x就是一个位置参数。当我们调用power函数时，必须传入有且仅有的一个参数x：
    '''
    print(power(2))


    def power2(x, n=2):
        s = 1
        while n > 0:
            n = n - 1
            s = s * x
        return s


    print(power2(2, 3))
    print(power2(2))
    '''
        必选参数在前，默认参数在后，否则Python的解释器会报错
    '''


    def enrool(name, gender):
        print('name=', name)
        print('gender=', gender)


    enrool('Sarah', 'F')

    '''
         如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
    '''


    def enroll2(name, gender, age=6, city='Beijing'):
        print('name:', name)
        print('gender:', gender)
        print('age:', age)
        print('city:', city)


    '''
        调用函数时可以不按照参数顺序调用，加上参数名字即可
        同scala
    '''
    enroll2('Adam', 'M', city='Tianjin')

    '''
        默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
        先定义一个函数，传入一个list，添加一个END再返回：
        这是因为L指向一个可变对象，定义的时候就定义为[] ，第二次调用时L指向的对象发生改变已经不是[]
        所以定义默认参数必须定义非可变对象比如none、str、
    '''


    def add_end(L=[]):
        L.append('End')
        return L


    def add_end2(L=None):
        if L is None:
            L = []
        L.append('End')
        return L


    li = add_end([1, 2, 3])
    print(li)
    print(add_end())  # ['End']
    print(add_end())  # ['End'] ['End']
    print(add_end2())  # ['End']

    '''
        可变参数
        定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
    '''


    # 方式一
    def calc(numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum

        # 但是调用的时候，需要先组装出一个list或tuple：


    print(calc(([1, 2, 3])))


    # 方式二
    def calc2(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum


    print(calc2(1, 2, 3))
    '''
        方式二与方式一实现的是相同的功能，与普通函数相比可变参数就是参数前面加个“*”
        如此可以接受任意多个参数包括一个，实际相当于传入一个list或者tuple
        如果是一个list或者tuple调用可变参数函数允许list前面加个*调用
        nums = [1, 2, 3]  calc2(*nums)
    '''

    '''
        关键字参数:
        可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
        而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    '''


    def person(name, age, **kw):
        print('name:', name, 'age:', age, 'other:', kw)


    # 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
    print(person('Michael', 30))  # name: Michael age: 30 other: {}   第二行打印：None
    # 也可以传入任意个数的关键字参数：
    print(person('Bob', 35, city='Beijing'))
    person('Adam', 45, gender='M', job='Engineer')
    # 当然，上面复杂的调用可以用简化的写法：
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    print(person('Jack', 24, **extra))

    '''
        命名关键字参数:
            对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
            仍以person()函数为例，我们希望检查是否有city和job参数：
             def person(name, age, **kw):
                if 'city' in kw:
                    # 有city参数
                    pass
                if 'job' in kw:
                    # 有job参数
                    pass
                print('name:', name, 'age:', age, 'other:', kw)
            person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
            但是调用者仍可以传入不受限制的关键字参数
            如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
            def person(name, age, *, city, job):
                print(name, age, city, job)
            和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
            person('Jack', 24, city='Beijing', job='Engineer')  # Jack 24 Beijing Engineer
            命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
            person('Jack', 24, 'Beijing', 'Engineer')
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: person() takes 2 positional arguments but 4 were given
            由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
            命名关键字参数可以有缺省值，从而简化调用：
            def person(name, age, *, city='Beijing', job):
                print(name, age, city, job)
            person('Jack', 24, job='Engineer')
            使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
            def person(name, age, city, job):
                # 缺少 *，city和job被视为位置参数
                pass

    '''

    '''
        参数组合:
            在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
            这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。但是请注意，
            参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
            比如定义一个函数，包含上述若干种参数：
            def f1(a, b, c=0, *args, **kw):
                print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

            def f2(a, b, c=0, *, d, **kw):
                print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
            在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
            >>> f1(1, 2)
            a = 1 b = 2 c = 0 args = () kw = {}
            >>> f1(1, 2, c=3)
            a = 1 b = 2 c = 3 args = () kw = {}
            >>> f1(1, 2, 3, 'a', 'b')
            a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
            >>> f1(1, 2, 3, 'a', 'b', x=99)
            a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
            >>> f2(1, 2, d=99, ext=None)
            a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
            最神奇的是通过一个tuple和dict，你也可以调用上述函数：
            >>> args = (1, 2, 3, 4)
            >>> kw = {'d': 99, 'x': '#'}
            >>> f1(*args, **kw)
            a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
            >>> args = (1, 2, 3)
            >>> kw = {'d': 88, 'x': '#'}
            >>> f2(*args, **kw)
            a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
            所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
    '''


    '''
        小结:
            Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
            默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
            要注意定义可变参数和关键字参数的语法：
            *args是可变参数，args接收的是一个tuple；
            **kw是关键字参数，kw接收的是一个dict。
            以及调用函数时如何传入可变参数和关键字参数的语法：
            可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
            关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
            使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
            命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
            定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
    '''
