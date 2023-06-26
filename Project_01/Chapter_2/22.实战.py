# coding:utf-8

num = eval(input('请输入一个四位整数：'))
sd = num%10 #个位
tens = num//10%10 #十位数字
hundred = num//100%10 #百位数字
thousands = num//1000 #千位数字
print('千位数字：',thousands)
print('百位数字：',hundred)
print('十位数字：',tens)
print('个位数字：',sd)
print('------------------------------------------------------')
father = eval(input('父亲身高：'))
mother = eval(input('母亲身高：'))
son = (father+mother)*0.54
print('预测儿子身高为：',round(son,2)) #float类型可能产生不确定位数，用round限制




