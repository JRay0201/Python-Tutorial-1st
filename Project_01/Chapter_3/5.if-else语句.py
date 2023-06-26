# coding:utf-8

number=eval(input('请输入数字：'))
#使用if-else语句
if number==12345:
    print('恭喜你中奖了')
else:
    print("未中奖")

print('-------使用条件表达式简化-------')
result ='恭喜你中奖了'if number == 12345 else "未中奖"
print(result)