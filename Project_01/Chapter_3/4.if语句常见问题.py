# coding:utf-8
#常见问题：
#1.if语句后面少了冒号；
#2.缩进问题：语句块如果为多句代码，则缩进要保持一致；


number=eval(input('请输入数字：'))
#使用if语句
if number==9876:
    print('恭喜你中奖了')
if number!=9876:
    print("未中奖")

print('---------以上if判读的表达式，使用的是比较运算符------------')
n=98
if n%2: #98%2的余数为0,即False
    print(n,'为奇数')
if not n%2:
    print(n,'为偶数')
print('---------判断一个字符串是否为空字符串-----------')
x=input('请输入一个字符串：') #空字符串的bool值为False
if x:
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')
print('---------表达式可以是一个单纯的变量-----------')
flag=eval(input('请输入一个布尔类型的值：'))
if  flag:
    print('flag的值为True')
if not flag:
    print('flag的值为False')
print('---------使用if语句时，如果只有一句语句块，可直接写在冒号后面-----------')
a=10
b=5
if a>b:max=a
print('a和b的最大值为：',max)
