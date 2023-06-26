# coding:utf-8
i=0
while i<3 :
    user_name=input('用户名：')
    pwd=input('密码：')
    #判断
    if user_name=='jl' and pwd=='123123':
        print('系统登陆成功')
        #改变循环条件，退出循环
        i=100
    else:
        if i<2:
            print('用户名或密码错误,还有',2-i,'次机会')
        else:
            print('机会用完！')
        i+=1

