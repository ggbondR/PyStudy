# 井号开头的行，用于写单行注释，注释仅用于开发者查看，不影响代码执行
# 三个单引号，或者三个双引号，用于多行注释，本脚本的末尾使用三个双引号注释多行

# L1、print(), input() 的使用, 以及向文件中打印内容
# 功能：打印出你想看的内容
# 目标：学会使用print(), input()
# 进阶目标：学会查看print()的函数定义，体验如何查看api文档

a = 'hello world'  # 使用单引号包住一串字符
print(a)  # 想看看a是什么，打印出来，即变量a的内容
print('hello world')  # 也可以直接打印一串字符

b = 1 + 1
print(b)  # 也可以打印数字,这里是变量b的值
print('b')  # 注意这样写和上面的区别，这样是打印一个字符'b'

print(a, b, 123, 'orion star')  # 可以同时打印多个内容，逗号隔开，注意观察输出的效果
print(a, b, 123, 'orion star', sep=', ')  # 注意和上一行的效果的区别

print(a)
print(b)
print(a, end='...')  # 打印a，但是结尾不换行
print(b)  # 注意观察b打印出来的效果，和上面的a在同一行，被'...'隔开

c = input()  # 等待用户输入内容，把结果赋给c
print(c)  # 把c再打印出来
# d = int(c)
print(c * 2)

outputFile = open('./test.pdf', 'w')
print('hello world', 123, sep=',', end='\n', file=outputFile)
print('hi', 456, sep=',', end='\n', file=outputFile)
# 补充知识：
# 补充知识不影响学习python，用于进阶提升编程能力的，有时会用到一点后面的内容。
# 学完我们会复习一遍所学，回过头来看补充知识。
"""
pycharm中，可以ctrl（mac里是cmd?）+单击print函数，查看到print函数定义文档
函数定义如下，
print(*args, sep=' ', end='\n', file=None)
sep 多个打印元素时，指定使用什么隔开，默认是一个空格
end 打印完最后一个元素后，追加一个什么内容，默认是换行符 ’\n‘
file 指定打印到哪个文件，可以指定某个文件流，默认是标准输入输出设备（std.out,电脑上就是屏幕）
上面的知识点，都可以根据查看函数原型了解。

比如将来python版本更新，知识点可能就不再适用了，
此时要以新版 函数原型描述（即api文档）为准。
"""
