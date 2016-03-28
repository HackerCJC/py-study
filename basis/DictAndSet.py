#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
if __name__ == '__main__':
    """
        python 内置了字典，相当于其它语言中的Map，dict全称dictionary
        使用键值形式存储。具有极快的查找速度 ......

    """
    # 根据名字查找成绩
    d = {'michael': 95, 'Bob': 75, 'Tracy': 85}
    # print(d['michael'])
    """
        为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，
        我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

        第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。
        无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

        dict就是第二种实现方式，给定一个名字，比如'Michael'，
        dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

        你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。

        把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

    """
    d['adam'] = 67  # 添加元素
    print(d)

    '''
     由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
   '''
    d['Jack'] = 90
    print(d['Jack'])
    d['Jack'] = 80
    print(d['Jack'])
    '''
    如果key不存在，dict就会报错
    '''
    # print(d['Thomas'])

    '''
     要避免key不存在的错误，有两种办法，
     一是通过in判断key是否存在
     二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
     None == null
   '''
    print('Thomas' in d)  # False
    print(d.get('Thomas'))
    print(d.get('Thomas', 234567))
    '''
    要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
   '''
    print('drop before: ', d)
    d.pop('Jack')
    print('drop after: ', d)
    '''
        dict 内部的存放顺序和key无关，俗称无序
        dict和list比较
            dict不会随着存放元素的增多，查找和插入顺序变慢，list会
            dict相比list更占用空间，是以空间换时间
        dict适用于高速查找场景
        需要注意：key必须是不可变对象，因为dict需要根据key计算value的位置，如果key可变会造成混乱
        这种根据key计算value位置的算法俗称hash算法
        python中字符串、数字类型都是不可变对象，list是可变对象不能作为dict的key
    '''

    # list_key = [1, 2, 3]
    # d[list_key] = 'a list'    list 不能做key  TypeError: unhashable type: 'list'
    # print(d)

    # d2 = {1: 2, 2: 3}
    # print(d2[1])
    # print(d2[2])


    '''
     set: set和dict 想类似，只不过不存储value
          set中元素是无序的，创建set内部需要先创建一个list
          set中元素不能重复，重复元素会自动过滤掉
    '''
    s = set([1, 2, 3])
    s = set([2, 3, 2, 45, 66])
    print(s)
    # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
    s.add(33)
    s.add(33)
    print(s)
    # 通过remove(key)方法可以删除元素：
    s.remove(33)
    print(s)
    # set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s1 & s2)  # 交集
    print(s1 | s2)  # 并集

    '''
        set 和 dict 的原理是一样的，因此不可以放入可变对象，因为放入可变对象
        无法判断两个对象是否相等，就无法保证set内部没有重复元素
        str 是不可变对象，list是可变对象
    '''
    a = ['c', 'a', 'b']
    a.sort()  # 对list进行了排序，改变了list中的元素顺序
    print(a)
    a = 'abc'
    b = a.replace('a', 'A')  # str的值并没有改变，而是产生了一个新的str
    print(b)
    print(a)
    s2 = set([(1, 2, 3)])
    # s2 = set([(1, [2, 3])])  list 是可变对象不能放入set中
    print(s2)

    '''
    小结

        使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

        tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
    '''
