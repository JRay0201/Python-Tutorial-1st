# coding:utf-8
#while语法结构：
# while 表达式：
#   语句块

#1.初始化变量
answer=input('今天上课吗？y/n')
while answer=='y':  #2.条件判断
    print('今天要上课！') #3.语句块
    #4.改变变量
    answer=input('今天上课吗？y/n')

#1~100之间的累加和
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print('1~100之间的累加和:',sum)





