# coding:utf-8
answer=input('请问你喝酒了吗？y/n')
if answer=='y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('酒精含量低')
    elif proof<80:
        print('构成酒驾标准，请不要开车')
    else:
        print('构成醉驾标准！！！')
else:
    print('未喝酒可离开')