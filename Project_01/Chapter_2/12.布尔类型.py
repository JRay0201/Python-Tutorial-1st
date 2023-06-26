#布尔类型
#所有对象都有一个布尔值，使用内置函数bool()进行测试

x=True
y=False

print(x+10) #1+10
print(y+10) #0+10

#布尔值为假的情况
#False 或者 None
#数值中的0，包含0 , 0.0 , 虚数0
#空序列，包含空字符串，空元组，空列表，空字典
#自定义对象的实例，该对象的__bool__()方法返回False 或者 __len__()方法返回0
print('-------------------------------------------')
#总结：非0的数值型布尔值都为True
print(bool(18))
print(bool(0) , bool(0.0))


print(bool('JRay'))
print(bool(''))


