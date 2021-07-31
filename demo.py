#!/usr/bin/python
a = 10
print(a)
# type方法可以打印值得类型
# python的数据
# 类型 int类型 tuple类型  String（字符型） List（列表类型） Dictonary（字典类型）
# 元组不能二次赋值，但列表可以
print(type(a))
b = 'ywh'
print(type(b))
c = ['a','b','c']
print(type(c))
d=('a','b','c')
print(type(d))
for letter in 'Python':  # 第一个实例
    print("当前字母: %s" % letter)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 : %s' % fruits[index])

print("Good bye!")



