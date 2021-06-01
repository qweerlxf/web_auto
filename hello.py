print('hello world')

#对象
    #字符串对象
    #数字对象
    #所有的数据类型都是对象
        #字符串
        #数字：整数、小数
        #列表、字典
        #函数、类、模块

#变量 variable
    #人类语言：人、物体————名字
    #编程语言：对象————变量
    #a1=3
    #a1='hello world'
    #a1=100+34
        #给对象起了个名字
        #通过名字访问到对象
    #print（a1)

#变量的命名
    #一般以字母（大写，小写均可）开头
    #后面可以使用下划线_ 或者数字
        #My,my,myname,my_name,myName,name1,name2id
    #大小写敏感
        #my My
    #不能与关键字相同（关键字是python语言里面的特殊字符）
        #import=1
    #不要与内置函数相同
        #print=1    #已重新定义print含义
        #print('hello world')   #报错

#变量的重新赋值
a1=3
print(a1)

a1='abc'
print(a1)

#使用变量的好处：多次指代对象
a1='关键字是python语言里面的特殊字符,关键字是python语言里面的特殊字符,关键字是python语言里面的特殊字符'
print(a1)

#函数 function
#给一串动作起名字
#踢足球
def playfootball():
    print("拿起足球")
    print("来到球场上")
    print("分成两队")
    print("设法把球踢进对方球门")

print(playfootball)

playfootball()

#函数的调用与返回
#函数的定义要在函数的调用前面
def foo():
    print("in foo")
    a = 23*23
    b = a+24
    print(b)
print("step 1")
foo()

def func1():
    print('now we are in func1')

print('before func1')
func1()
print('after func1')

#函数的调用参数
#饮料机的例子
#饮料机一：
#只吐出可口可乐
#饮料机二：
#选择可乐种类
#可以吐出可口可乐、芬达、百事可乐

#定义参数（形参）时的命名规则 - 和变量一样
#可以是一个，可以是多个（逗号隔开）
#函数体里面像变量一样的使用参数
#调用函数时，传入对应个数的参数（实参）
def fool(x):
    print(x+3)
fool(3)

def foo2(a,b):
    print(a*3+b*5/23)
foo2(3,4)

def playfootball(members):
    print(members)
    print("拿起足球")
    print("来到球场上")
    print("分成两队")
    print("设法把球踢进对方球门")

playfootball('张三、李四、王二......')

#另一种参数传入的方式
foo2(a=3, b=4)
foo2(b=4, a=3)
foo2(3, b=4)
#foo2(a=3,4)    #错误写法
#规则
#次序可以颠倒
#一旦第n个参数使用了关键字参数，后面所有的参数都必须使用关键字

#函数的返回值
#return关键字
#返回对象可以赋值给变量，也可以直接使用
def foo1(x):
    return x+3
a = foo1(3)
a = foo1(3) + 54
print(foo1(3))
print(foo1(3)+54)

#字符串
#非常常用，非常高效
#C语言实现，高度优化
#定义：单引号,双引号，或者三引号
print("""hello world""")
#三引号的特点
var1 = '''Python is

tool
'''
#字符串里包含引号字符
#'it is "good"'

#拼接
#'my name is ' + 'jay'
#使用乘法符号两个字符串拼接
#重复n次
#'we'*3

#sequence操作
#字符串的特性 被称为sequence（序列）
#一个序列，若干个元素组成
#Sequence相同的操作

#位置索引index
#标志每个元素的位置
#用来获取元素

#从左到右，从0开始  0,1,...,n-1
#a[0],a[1],a[2]

#可以用正数表示，也可以用负数表示
#最后一个元素也可以是a[-1]    -n,-n+1,...,-1

#长度为n的字符串，最后一个元素a[n-1]

#可以是表达式
#aString = 'name:jack'
#aString[4+1]

#越界
#aString = 'abcd'
#aString[4]

#切片操作slice
#获取子字符串的切片操作
#截取slice字符串的一部分内容
#和索引一样，切片的操作符是[]
#参数有两个，中间以：隔开
#string1[start:end],从start开始，到end结束，但不包括end
#string1[start:],从start开始，到字符串结束
#string1[:end],从第一个字符开始，到end位置结束，但不包括end

#获取字符串的长度
#使用len函数
len("my bame is:")

#列表和元组
#列表 List
#字符串 是一种Sequence
#由一个个元素组成
#每个元素是一个字符
#列表也是一种Sequence类型
#可以存储任何类型的数据，每个元素是任意类型

#列表的定义和创建
#列表的元素
[]  #空列表
[1,1.333,'a','abc'] #四个元素
#也可以这样创建一个空列表
list()  #空列表

#包含列表的列表
aList = [123,
         'abc',
         4.56,['inner','list']]

aList[1:4]  #产生新的对象，原来的对象并没有改变

aList[3][1]

#列表的元素可以改变，而字符串不行

#元组tuple
#元组也是一种Sequence类型
#可以存储任何类型的数据，每个元素是任意类型
#元组和List非常相似，只有一个最大的不同
#元组不能改变其组成元素 immutable

a = (1,1.33,'abc')
a = 1,1.33,'abc'
a = (1,)    #单个元素元组
a = 1,    #单个元素元组
a = ()  #空元组
tuple() #空元组

