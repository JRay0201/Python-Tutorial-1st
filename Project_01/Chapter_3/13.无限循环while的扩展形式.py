# coding:utf-8
#while扩展语法结构：
# while 表达式：
#   语句块1
# else：
#   语句块2

#else语句只在循环结构后才执行


#1~100之间的累加和
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
else:
    print('1~100之间的累加和:',sum)