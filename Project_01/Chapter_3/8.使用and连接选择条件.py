# coding:utf-8
#使用and连接多个选择条件:只有同时满足多个条件，才能执行if后面的语句块

user_name=input('请输入您的用户名：')
pwd=input('请输入您的密码：')
if user_name=='jl' and pwd=='123123':
    print('登录成功')
else:
    print('用户名或密码错误')