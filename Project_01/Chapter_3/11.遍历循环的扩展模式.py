# coding:utf-8
#语法结构：
#   for 循环变量in 遍历对象:
#       语句块1
#   else:
#       语句块2

# else语句只在循环正常结束后才执行，通常与break和continue语句一起使用

#计算1~10之间的累加数和
s=0
for i in range(1,11):
    s+=i
else:
    print('s=',s)


