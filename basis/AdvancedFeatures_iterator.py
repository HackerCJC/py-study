#!/usr/bin/env python3
# ! __*__ coding=utf-8 __*__

'''python 高级特性之迭代器:与普通迭代不同
   python 凡是可以用for循环迭代的都是可迭代对象即Iterable，
   但iterable并非iterator，凡是可以用next()方法获取下一个元素的就是iterator
   list tuple dict set str 都是iterable不是iterator
   iterator 表示一个无限大的数据流，通过next方法可以不断获取其下一个元素直至没有元素抛出StopIteration
   iterator可以存储无限大自然数，list是永远不可能存储全体自然数的。计算是惰性的，只有需要返回下一个数据时才会计算
   iterable对象可以通过iter()方法转换为iterator对象
   python中for循环的本质就是iterator 通过不断调用next对象实现的
'''
if __name__ == '__main__':
    from collections import Iterable

    # 使用 isinstance可以判断对象是否是可迭代的
    print(isinstance([], Iterable))
    print(isinstance((), Iterable))
    print(isinstance({}, Iterable))
    print(isinstance(set(), Iterable))
    print(isinstance('A,B,C', Iterable))
    print(isinstance(100, Iterable))

    # 判断一个对象是否是 Iterator
    from collections import Iterator

    print((x for x in range(10)))
    print(isinstance((x for x in range(10)), Iterator))
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance(set(), Iterator))
    print(isinstance((), Iterator))
    print(isinstance('abc', Iterator))
    print(isinstance(100, Iterator))

    # 使用iter()方法可以把iterable对象转换为iterator
    print(isinstance(iter('abc'), Iterator))
    # print(isinstance(iter(123), Iterator)) # TypeError: 'int' object is not iterable


    '''
        Python的for循环本质上就是通过不断调用next()函数实现的，例如：
    '''
    for x in [1, 2, 3, 4, 5]:
        pass

    it = iter([1, 2, 3, 4, 5])
    while True:
        try:
            # 获得下一个值:
            x = next(it)
        except StopIteration as e:
            # 遇到StopIteration就退出循环
            break

    '''
        小结
            凡是可作用于for循环的对象都是Iterable类型；
            凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
            集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
            Python的for循环本质上就是通过不断调用next()函数实现的，例如：
    '''
