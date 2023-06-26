# coding:utf-8
#遍历循环for
#语法结构：
#   for 循环变量in 遍历对象：
#       语句块

#遍历对象：字符串，文件，组合数据类型，range()函数等

for i in 'hello':
    print(i)

#range()函数，产生一个[n,m)的整数序列，包含n，不包含m
for i in range(1,11):
    #print(i)
    if i%2==0:
        print(i,'是偶数')

#计算1~10之间的累加数和
s=0
for i in range(1,11):
    s+=i
print('s=',s)

'''
153 = 3*3*3+5*5*5*+1*1*1
'''
print('----------计算100~999之间的水仙花数---------')
for i in range(100,1000):
    sd=i%10 #获取个位数
    tens = i//10%10 #获取十位数
    hunderd=i//100  #获取百位数
    if sd**3 + tens**3 +hunderd**3 ==i:
        print('水仙花数为：',i)
print('--------除以 和 整除 的区别-------------')
print(153/10%10)
print(153//10%10)