# coding:utf-8
#逻辑运算符是对真假两种布尔值进行运算，运算结果仍是一种布尔值
#运算符    含义      用法                  结合方向
# and    逻辑与   表达式1 and 表达式2        从左到右 ->
# or     逻辑或   表达式1 or  表达式2        从左到右 ->
# not    逻辑非   not 表达式1               从右到左 <-

print(True and True)
print(True or False)
print(not True)
print(8<7 and 10/0) #逻辑与中，当第一个表达式为假时，第二个表达式不计算

print(8>7 or 10/0) #逻辑或中，当第一个表达式为真时，第二个表达式不计算


