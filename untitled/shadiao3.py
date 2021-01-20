age = 20

if age > 18:
    print("年龄已经到了18")
    print('default ==== ')
    print('66666')
else:
    print('年龄不足')

print('========================================')
# for循环
names = ['michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for i in [1, 2, 3, 4, 5, 6, 7]:
    sum = sum + i
print(sum)


#range生成0-1000的数组
ranList = list(range(1000))
sum1 = 0
for d in ranList:
    sum1 = sum1 + d
print(sum1)

#break跳出整个循环
n = 0

while n < 10:
    n = n + 1
    if n > 10:
        break
    print(n)
#continue跳过当前的这次循环，开始下一次的循环

print('================================================')
f = 0
while f < 10:
    f = f + 1
    if f == 6:
        continue
    print(f)












