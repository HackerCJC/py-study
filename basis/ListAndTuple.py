#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
    list 列表 ： 一种有序的集合可以随时添加和删除其中的元素
    tuple 元组 ： 有序列表
'''

if __name__ == '__main__':
    #  1、  list列表常用操作
    '''
    classMates = ['Michael', 'Bod', 'Tracy']
    print(classMates)
    print(len(classMates))#打印列表长度
    print(classMates[0]) #访问集合元素角标从0开始
    print(classMates[-1])# 访问最后一个元素
    print(classMates[-2])# 访问倒数第二个元素
    print(classMates[len(classMates)-1])# 访问最后一个元素
    classMates.insert(1,'Jack') # 向指定索引插入元素
    classMates.pop() # 删除list末尾元素
    classMates.pop(1) # 删除指定索引位置元素
    classMates[0] = 'Leo'  # 把指定索引元素替换成某个元素
    L = ['Apple', 123, True]  # list中的元素类型也可以不同
    # print(classMates)
    s = ['python', 'java', ['asp', 'php'], 'scheme']  # list中的元素也可以是list
    # print(len(s))
    # 两种方式那倒php
    p = ['asp', 'php']
    s2 = ['python', 'java', p, 'scheme']
    print(p[1])
    print(s2[2][1])
    l = [] # 空list
    print(len(l))
     '''

    # 2、tuple常用操作,tuple和list十分相似,但tuple一旦初始化就不能修改
    '''
      classMates = ('michael', 'Bob', 'Tracy')
      # classMates[0]='cui0'  不能改变tuple的元素
      # print(classMates)
      # t=(1,2)
      # print(t)
      t = ()  # 定义空tuple
      # * 注意tuple的一个陷阱
      t = (1)  # 这个小括号是数学表达式 这样定义代表1这个数字，python规定定义一个元素的tuple需要(1,)
      t = (1,)
      print(t)

      # 可变tuple ， 实际改变的是tuple中list的元素，tuple中元素的指向并未改变
      # 因此要创建不可变tuple,只需保证tuple中元素也不可变即可
      t = ('a', 'b', ['A', 'B'])
      print('--- 改变前', t)
      t[2][0] = 'X'
      t[2][1] = 'Y'
      print('--- 改变后', t)
      '''
    # 练习
    # 请用索引取出下面list的指定元素：
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    # 打印Apple:
    print(L[0][0])
    # 打印Python:
    print(L[1][1])
    # 打印Lisa:
    print(L[2][2])
    '''
    小结

    list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
    '''
