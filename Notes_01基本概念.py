# 01.01注释
# 你好这是单行注释（#号后面建议空格符合python规范）
"""
你好这是多行注释（也可以单行使用）
"""

# 01.02打印
print(666)
print(13.14)
print("TEST")
print("hello", end='')# 不换行
print("world")
print("hello\tworld")#对齐 8 字符
print("iamfxy\tfxy")

# 01.03定义变量
money = 50
print("v我", money)
money = money - 10
print("buy KFC, i still have", money, "$")

# 01.04type()查看数据类型
# print语句直接输出类型信息
print(type("fxy"))
print(type(666))
print(type(13.14))
print(type(True))

# 用遍量存储type()
string_type = type("fxy")
int_type = type(666)
print(string_type)
print(int_type)

# 查看变量类型
name = "fxy"
name_type = type(name)
print(name_type)

# 01.05转换类型
# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str))
print(num_str)

# 将字符串转换成数字类型
num1 = int("11")
print(type(num1))
print(num1)

num2 = float("1.1")
print(type(num2))
print(num2)

# 整数转浮点数
float_num = float(11)
print(type(float_num))
print(float_num)

# 浮点数转整数
int_num = int(11.745)
print(type(int_num))
print(int_num)# 11

# 01.06标识符
# 英文、中文、数字、下划线_

# 01.07运算符
# +
# -
# *
# /
# %取余
# **指数
# //结果取整

# 复合运算符+=等等和java一个道理

# 01.08字符串
# \用此符号转义

# 使用+号拼接字符串（只可拼接字符串，不可拼接非字符串类型）

# 01.09字符串格式化
# 第一种方法 %占位符拼接
money1 = 100
money2 = 10
message1 = "我有 %s 块" % money1
message2 = "我有 %s 块，花了 %f 块" % (money1, money2)
print(message1)
print(message2)
# %s 将内容转换为字符串占位
# %d 将内容转换为整数占位
# %f 将内容转换为浮点数占位

# 字符串格式化第一种方法的数字精度控制
# m控制宽度（如果比数字本身宽度小，则m失效）
# .n控制小数精度
# %5d e.g. 11 变为   11(前面有3个空格)
# %5.2d e.g. 11.345 变为  11.35(前面2个空格一共7位，小数点后2位)
# %.2f e.g. 11.345 变为11.35

# 第二种方法 f"我是{name}"
print(f"我是{name}")

# 01.10数据输入input
print("请输入你的名字1")
user_name1 = input()
print("我的名字是 %s" % user_name1)

user_name2 = input("请输入你的名字2")
print("我的名字是 %s" % user_name2)

# 输入的一定为string类型，其他类型需要转换
num = int(input("请输入你要取多少钱"))
print(type(num))

# 01.11比较运算符
# ==
# !=
# <
# >
# <=
# >=

# 01.12boolean
flag = 10 > 5
print(flag)
print(type(flag))

# 01.13if判断语句
# 1.判断条件
# 2.冒号:
# 3.需要缩进4个空格，否则和if是并列的
age = 30
if age >= 18:
    print("你已经成年了")
elif age >= 50:
    print(f"你的年纪为{name}")
else:
    print("你未成年")
print("12345")

# 01.14while循环
i = 0
while i < 5:
    print(i)
    i = i + 1

# 01.15for循环
name_xxx = "fxy"
for i in name_xxx:
    print(i)

# range语句
# 0到4
# range(5) = [0, 1, 2, 3, 4]
# 1到4
# range(1, 5) = [1, 2, 3, 4]
# 1到4，步长每隔2取一个
# range(1, 5, 2) = [1, 3]

# while和for循环写九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%s * %s = %s\t" % (j, i, i * j), end=' ')
        j += 1
    print()
    i += 1

for k in range(1, 10):
    for l in range(1, k+1):
        print(f"{l} * {k} = {k * l}\t", end=' ')
    print()

# 01.16continue和break
# 和java作用一致