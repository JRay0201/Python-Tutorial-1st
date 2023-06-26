#数据类型之间的转换
#隐式类型转换：通过数学运算可以隐式将int 类型转换float类型

x=10
y=3
z = x/y #隐式转换
print('Z\'s Type is ',type(z),' , z = ' , z)

#显示类型转换
"""
int(x)      转为整数
float(x)    转为浮点数
str(x)      转为字符串
chr(x)      将整数x转为一个字符
ord(x)      将一个字符x转为其对应的整数值
hex(x)      将一个整数x转为一个十六进制字符串
oct(x)      将一个整数x转为一个八进制字符串
bin(x)      将一个整数x转为一个二进制字符串
"""
#float类型转成int类型,只保留整数部分
print('float类型转成int类型',int(3.14))
print('float类型转成int类型',int(3.9))
print('float类型转成int类型',int(-3.19))
print('float类型转成int类型',int(-3.9))
print('--------------------------------------')

#int类型转成float类型
print('int类型转成float类型' , float(10))
print('--------------------------------------')

#str类型转成int类型
print('str类型转成int类型' , int('100') + int('200'))
print('--------------------------------------')

#str类型转成float类型
print('str类型转成float类型' , float('3.14'))
print('--------------------------------------')

#str转成int类型报错的情况
#print(int('18a')) #ValueError: invalid literal for int() with base 10: '18a'

#print(int('3.14')) #ValueError: invalid literal for int() with base 10: '3.14'

#str转成float类型报错的情况
#print(float('34a.1'))

#chr() 与 ord()函数 , 互为相反操作
print(ord('金'))
print(chr(37329))
print('--------------------------------------')

#进制之间的转换操作 ， 十进制与其他进制之间的转换
print('十进制转十六进制：' , hex(37329))
print('十进制转八进制：' , oct(37329))
print('十进制转二进制：' , bin(37329))

