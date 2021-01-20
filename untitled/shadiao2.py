
a = 100
b = 200
pi = 3.14159
url = "https://www.baidu.com"
real = True



print('%d' % a)
print('%d' % (a + b))

print('=============================================\n')

print('%s' % url)
print('%f' % pi)
print(type(pi))

print('=============================================\n')
#有序集合可以随时添加和删除元素
myList = ['java', 'android', 'ios']

#打印出集合中元素的个数，list的索引是从0开始的， 最后一个元素的索引是len(myList) -1
print(len(myList))

#用-1索引直接获取最后一个元素， -2为倒数第二个，倒数也是有可能越界的
print(myList[-1])

#追加元素
myList.append('c++')
print(myList)

#指定位置插入元素
myList.insert(1, 'python')
print(myList)

#删除末尾的元素。pop(int),也可以删除指定位置的，小心越界
myList.pop()
print(myList)

#元素赋值,可以赋值不同类型的
myList[1] = 'hello'
print(myList)

#空的list
emptyList = []

#二维数组
doubleList = ['嘻嘻', '哈哈', ['鲁班', '女娲', '阿狸', '王昭君'],'heihei', 'dalao']
print(doubleList)

double1List = ['二狗', '水果']
double2List = ['人才', '甄姬', double1List, '旺仔']
print(double2List)

#元组
print('===================================================================\n')
#tuple一旦初始化就不能修改，不能插入，赋值，和追加元素,并且初始化就的把元素确定下来
tuple1 = (1, 2, 3, 4)
print(tuple1)

#定义一个空的tuple
tuple2 = ()
print(tuple2)

#定义一个元素的tuple,加，来区分歧义
tuple3 = (1, )
print(tuple3)

#可变的tuple
tuple4 = (1, 2, ['heihei', '我草'])
print(tuple4)






