#!/usr/bin/env python3
# ! __*__ coding=utf-8 __*__
'python 高级特性之迭代: 列表生成式'
if __name__ == '__main__':
    '''
     列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
     举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
   '''
    print([x * x for x in range(1, 11)])
    print([x * x for x in range(1, 11) if x % 2 == 0])  ## 类似于scala中的守卫
    '可以使用两层for循环，生成全排列'
    print([m + n for m in 'ABC' for n in 'XYZ'])
    '三层或三层以上的for循环很少使用'

    '利用列表生成式可以写出非常简洁的代码，例如列出当前目录下的所有文件和目录名，可以通过一行代码实现'
    import os  # 导入os模块

    print([d for d in os.listdir('.')])
    '列表生成式，也可以使用两个变量来生成list'
    print([k + "=" + v for k, v in {'x': 'A', 'y': 'B', 'z': 'C'}.items()])

    '练习：把一个list中的所有字符串编程小写'
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([word.lower() for word in L])

    '''
       练习
        如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
        使用内建的isinstance函数可以判断一个变量是不是字符串：
        请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
    '''
    L = ['Hello', 'World', 18, 'Apple', None]
    print([word.lower() for word in L if isinstance(word, str)])  # word.lower 相当于打印函数对象 word.lower(）才是调用方法

    '''
     小结
        运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
    '''
