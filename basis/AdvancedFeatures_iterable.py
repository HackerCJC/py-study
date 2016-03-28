#!/usr/bin/env python3
# ! __*__ coding=utf-8 __*__
'python 高级特性之迭代: python 迭代是 for ... in这种形式，迭代的是可迭代对象不需要角标，比java for int i=0;i<arr.length i++ 更加深入'
if __name__ == '__main__':
    '迭代map'
    d = {'a': 1, 'b': 2, 'c': 3}
    '迭代map中的key,因为dict中的key是无序的，所以打印顺序无序'
    for key in d:
        print(key)
    '迭代map中的value'
    for val in d.values():
        print(val)
    '迭代map中的key和value'
    for item in d.items():
        print(item)
    '迭代字符串'
    for ch in 'ABC':
        print(ch)
    'python 迭代可迭代对象，如何判断一个对象是否可以迭代呢？ 通过collections模块的iterabel判断：'
    from collections import Iterable

    print(isinstance('abc', Iterable))  # str 是否可以迭代
    print(isinstance([1, 2, 3], Iterable))  # list 是否可以迭代
    print(isinstance(123, Iterable))  # 整数是否可以迭代

    '如果要像java那样取出list中元素的下标，可以使用python内置的enumerate,这样既可以取出元素下标，又可以取出元素本身'
    for i, value in enumerate([1, 2, 3]):
        print(i, value)

    'for 循环里同时引用两个变量，在python中非常常见，'
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)

    '''
        小结:
        任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
    '''
