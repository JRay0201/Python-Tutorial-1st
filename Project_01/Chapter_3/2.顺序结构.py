# coding:utf-8
#复制运算符的执行顺序是从右到左
name='张三'
age=20
a=b=c=100
#系列解包赋值
name1,age1="li",22 #元组分解赋值
print(name1,age1)
[name2,age2] = ['JJJ',30] #列表分解赋值
print(name2,age2)
a,b,c,d = 'room' #字符串分解赋值
print(a,b,c,d)

#扩展的字符串解包赋值
a,*b='banana'
print(a,b)

print('------输入输出语句，也是典型的顺序结构----------')
name4 = input('name=')
age4=eval(input('age='))
print('name = ',name4)
print('age=',age4)
