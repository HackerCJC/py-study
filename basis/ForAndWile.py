#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    '''
        把每个元素带入变量name
        names = ['Michael', 'Bob', 'Tracy']
        for name in names:
            print(name)
    '''
    '''
        sum = 0
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            sum += x
        print(sum)
    '''
    '''
        range() 函数可以生成从0开始的序列,list()函数可以把range转换为list

        sum = 0
        ontTo100 = list(range(5))
        print(ontTo100)
        for x in ontTo100:
            sum += x
        print(sum)
    '''
    # while 循环
    '''
        sum = 0
        n = 99
        while n > 0:
            sum = sum + n
            n = n - 2
        print(sum)
    '''

    '''
    练习

    请利用循环依次对list中的每个名字打印出Hello, xxx!：

    '''

    L = ['Bart', 'Lisa', 'Adam']
    for x in L:
        print('hello,', x)

    '''
        小结

        循环是让计算机做重复任务的有效的方法，有些时候，如果代码写得有问题，会让程序陷入“死循环”，
        也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

        请试写一个死循环程序

    '''
