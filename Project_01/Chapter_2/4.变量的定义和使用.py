#1.变量的定义： 变量名=value
#2.Python是一种动态类型的语言，变量的类型可以随时变化，使用内置函数type()可以查看变量的数据类型
#3.允许多个变量指向同一个值，使用内置函数id()可以 返回变量所指的内存地址

#1.
luck_number = 8
my_name = 'JRay'
print('luck_number的数据类型是：' , type(luck_number))
print('my_name的数据类型是：' , type(my_name))

#2.通过赋不同的值直接修改变量类型
luck_number = '8'
print('luck_number的数据类型是：' , type(luck_number))

#3.允许多个变量指向同一个值
no = number = 1024
print('id内存地址为：' , id(no))
print('number内存地址为：' , id(number))
