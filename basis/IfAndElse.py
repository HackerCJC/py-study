#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    '''
  age = 7
  if age >= 18:
      print("your age is", age)
      print("audit")
  elif age >= 6:
      print("teenager")
  else:
      print("your age is", age)
      print("kid")

  if 的完整形式如下：

      if的执行特点是只要有一个判断条件成立，就不往下继续走了。if从上向下判断
  if <条件判断1>:
      <执行1>
  elif <条件判断2>:
      <执行2>
  elif <条件判断3>:
      <执行3>
  else:
      <执行4>
  '''
    # 只要x是非零数字，非空字符串，非空list、tuple 就判断为true否在判断为false
    '''
        x = 99  # TRUE
        x = []  # False
        x = ()  # False
        x = ''  # False
        if x:
            print('True')
        else:
            print('False')

        s = input('birth: ')
        birth = int(s)
        if birth < 2000:
            print('00前')
        else:
            print('00后')
    '''
    '''
    练习

        小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

        低于18.5：过轻
        18.5-25：正常
        25-28：过重
        28-32：肥胖
        高于32：严重肥胖
    '''
    height = 1.75
    weight = 80.5
    BMI = weight / height * height
    if BMI < 18.5:
        print("过轻")
    elif BMI >= 18.5 and BMI <= 25:
        print("正常")
    elif BMI > 25 and BMI <= 28:
        print("过重")
    elif BMI >= 28 and BMI <= 32:
        print("肥胖")
    else:
        print("严重肥胖")
        
        '''
        小结

        条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。

      '''
