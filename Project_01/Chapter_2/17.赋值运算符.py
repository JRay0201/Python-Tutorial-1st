# coding:utf-8
#赋值运算符：主要用于为变量进行赋值
#运算符    示例      展开形式
#  =      x=y       x=y
#  +=     x+=y      x=x+y
#  -=     x-=y      x=x-y
#  *=     x*=y      x=x*y
#  /=     x/=y      x=x/y
#  %=     x%=y      x=x%y
#  **=    x**=y     x=x**y
#  //=    x//=y     x=x//y

#python支持链式赋值
a=b=c=100
print(a,b,c)

#系列解包赋值
a,b=10,20
print(a,b)
print('----------如何交换两个变量的值-------------')
#不需创建临时变量
b,a=a,b
print(a,b)