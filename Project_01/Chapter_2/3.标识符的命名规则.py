my_name_1='JRay' #字母 数字 下划线 但数字不可以开头
My_name_1='ARailay' #标识符严格区分大小写
print(my_name_1)
print(My_name_1)
姓名 = 'JL' #可使用中文，但不建议
print(姓名)

#类名采用单词首字母大写形式（Pascal风格） 内部类采用”_“ + Pascal风格的类命名组成
class MyClass:
    class _InnerClass:
        pass
#函数，类的属性和方法的命名全部用小写字母，多个字母直接使用下划线分隔
def fun():
    pass
def fun_name():
    pass

#常量命名时采用全部大写字母，可使用下划线
PI=3.1415

#使用单下划线开头的模块变量或函数是受保护的，在使用”from xxx import*“语句从模块导入时，这些模块变量或函数不能被导入
#使用”__“双下划线开头的实例变量或方法是类私有的
#以双下划线开头和结尾的是Python的专用标识，例如：__init__()表示初始化函数