# 1.打印一行提示信息，如下
# please input your name
# 2.等待用户输入姓名
# 3.打印一行提示信息，如下
# please input your height in centimeter
# 4.等待用户输入身高
# 5.打印出用户的姓名和身高,用冒号隔开


# 示例
print('please input your name')
userName = input()
print('please input your height in centimeter')
userHeight = input()
print(userName, userHeight, sep=':')
# print(userName, ':', userHeight) 两种写法均可
