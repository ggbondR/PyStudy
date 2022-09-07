import sys
# L2、python中的变量
# 目标：1.python中变量的标志符规则
#      2.python中变量与内存（变量是如何存储的）
#      3.熟悉几类python变量，string, numbers (只学int, float), list,bool,list,dictionary,tuple,set
#      4.数据类型转换

"""
"""

"""
1.标志符
标识符由字母、数字、下划线组成, 但不能以数字开头。
以下划线开头的标识符是有特殊意义的，以后再说。
保留字符：
and, if, id, while, import等等，这些是python中已经使用过的单词，把它们作为变量标志符会带来歧义。
如： lightColor = 'red' 将'red'字符串赋值给了一个变量，变量的标志符叫做lightColor，正确
    and = 'red' 将'red'字符串赋值给了一个变量，变量的标志符叫做and，是保留字，错误。

# 补充知识：
好的命名规则，便于将来阅读维护代码。比如，可以二选一
A.驼峰命名，robotLightColor
B.下划线命名，robot_light_color
切记不要命名成 a, b, c, d，这样过一段时间，就不记得变量的含义了，导致代码阅读困难
"""

"""
2.变量与内存
科普tips:
计算机中，所有信息都是通过0,1的组合来存储的，
这是因为目前人们的"数字电路"中设计成晶体管两侧电压只有两种状态, 比如0V和5V，这样稳定且方便管理。
我们将0V记作状态0；5V记作状态1；这样每个晶体管就有两种状态了，千千万万个晶体管就可以记录很多信息了。
未来可能会有更高级的表示方式，比如量子计算机中，可能状态就不止2种了，这个暂时咱也不用管。

一个晶体管有两种状态，可以记录的信息量是1 bit（bit的严格定义在’信息论‘中有描述，这里不用管）
两个晶体管有两位数字，信息量是2 bit，可以表示四种状态00,01,10,11
N个晶体管有N位数字，信息量是N bit，可以表示2^N种状态

8 bit = 1 byte (8位=1字节)，可以表示2^8=256种状态
1024 bytes = 1 KB, 1024 KB = 1 MB, 1024 MB = 1GB, 1024 GB = 1 TB

具体数据怎么存储的呢？
比如一个整数 5，C++中如下存储的，占用4个bytes，
00000000 00000000 00000000 0000101
python中对Numbers的表达原理更加复杂，我们这里就先不管了，但是也是类似上面的二进制表达的。
实在好奇，bin()函数可以获取二进制表达，使用bin(5)可以获取二进制表达
print(bin(5))即可, 这会告诉你5这个数字在python中究竟占了多少字节。
"""

"""
3.python变量--前言
               基本类型
中文名称   类型            说明             
整数      int         整数类型，-24，0，123等
实数      float       实数类型，也称浮点数（与它在计算机中的表示有关），1.234，2.0, -3.14
字符串    string      一串有序的字符，如 'hello', 'ni hao, 123! wo shi ab-cd', 通常用单引号或者双引号将他括起来
布尔      bool        用于逻辑运算，取值只能是True/False, 逻辑运算包括 且，或，非

               容器类型（可以容纳多个任意类型的元素）
列表      list        一串有序序列 [100, 'hi', 23.4, True, 100]
字典      dict        若干个无序的键值对key,value，{’name‘: lw, 'gender': female, 'math': 150}
元组      tuple       一串有序序列，且不可修改 ('lw', 'female', 150)
集合      set         无序且不可重复
"""
"""
4.python数据类型转换
int--float--string--bool可以互相转换

如 a = str(2.3)，将2.3转化为 '2.3'(这是3个字符组成的字符串)
b = float('2.3')，将'2.3'这三个字符，转化成2.3
其他非法输入，类型互相转换自行测试。
容器类型不能互相转换，都可以转化成字符串打印出来
"""

"""
int, float 型变量的运算
加减乘除，模(取余数)，取商
"""
# a = 17 % 3  # 模，取余数  2
# b = 17 // 3  # 取商  5
# c = 2**5  # 表示2的5次方

"""
int 和 float混合运算得到的是float
除法运算得到的是float
"""
# a = 1
# b = 2.0
# c = a + b
# print(type(a), type(b), type(c))
# d = 2 / 1
# print(type(d))

"""
float 的精度问题
"""
# print(0.1 + 0.2 - 0.3)

"""
bool型的运算
and, or, not
"""

"""
string类型的运算
仅支持 加法 和 整数乘
"""
# a = 'hello'
# b = 'world'
# print(a + b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# print(a * 2)

"""
string的特殊操作
1. 获取长度，len()
2. 根据位置，获取字符 s[k], 支持倒着数
3. string的replace,find,count
......
"""
a = str('hello world')
# print(len(a))
# print(a[5], a[len(a) // 2], a[-2])
# print(a)
# print(a[len(a)]) # 越界
a = a.replace('hello', 'hi')
print(a)
# print(b)
