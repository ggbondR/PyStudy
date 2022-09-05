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

