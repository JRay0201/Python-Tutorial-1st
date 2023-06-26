# eval()函数
#   eval(s)函数将去掉字符串s最外侧的引号，并按照Python语句方式执行去掉引号后的字符串；
#   语法格式：变量 = eval(字符串）;
#   eval()函数经常和 input()函数一起使用，用来获取用户输入的数值型；
#--------------------------------------------------------------------
s='3.14 + 3'
print(s,type(s))

x=eval(s) #去掉了引号，执行了加法运算
print(x , type(x))

#--------------------------------------------------------------------
age = eval(input('请输入您的年龄：'))
print(age,type(age))

#报错的情况：
#去掉引号后只剩下 hello ，前面如果有定义变量hello的话就不会报错
#print(eval('hello')) #NameError: name 'hello' is not defined. Did you mean: 'help'?
