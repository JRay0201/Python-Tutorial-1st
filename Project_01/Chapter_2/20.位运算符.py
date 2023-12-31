# coding:utf-8
#位运算符
#位运算是把数字看作二进制数来进行计算的，所以需要先将要执行运算的数据转换为二进制，然后才能进行执行运算

# ”位与“ & 运算
#两个操作数据的二进制表示，只有对应位都为1时结果才是1，否则为0
#   0000 0101
# & 0000 1100
#   0000 0100
print(12&8)

# ”位或“ | 运算
#两个操作数据的二进制表示，只有对应位都为0时结果才是0，否则为1
#   0000 0101
# | 0000 1100
#   0000 1101
print(4|8)

# ”位异或“ ^ 运算
#两个操作数据的二进制,同时为0或1，结果为0，否则为1
#   0000 0101
# ^ 0000 1100
#   0000 1001
print(31^22)

# ”位取反“ ~ 运算
#操作数据的二进制,1改为0.0改为1
#   0000 0101
# ~ 1111 1010
print(~123)

# ”左移位“ << 运算
# 将一个二进制数向左移动指定的位数，左边（高位端）溢出的位被丢弃，右边(低位端）的空位用0补充
# 左移位运算相当于乘以2的N次幂
#       0000 0010
#    00 0000 1000
#   溢出        左移后补0
print(2<<2) #将2向左移动2位 == 2*2**2
print(2<<3) #将2向左移动3位 == 2*2**3
print(3<<2) #将3向左移动2位 == 3*2**2

# ”右移位“ >> 运算
# 将一个二进制数向右移动指定的位数，右边(低位端）溢出的位被丢弃，左边（高位端）的空位端，如果最高位是0（正数）左侧填0，
#如果最高位位1（负数）。左侧填1
# 右移位运算相当于除以2的N次幂
#    0000 1000                   1000 1000
#    0000 0010 00                1100 0010 00
#   右移后补0   溢出               右移后补1   溢出
print(2>>2) #将2向右移动2位 == 2/2**2
print(-8>>3) #将-8向右移动3位 ==-8/2**3
print(8>>2) #将8向右移动2位 == 8/2**2



