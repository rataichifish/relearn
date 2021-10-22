# 今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？
print("1、今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
number = int(input("请输入您认为符合条件的数："))     # 输入一个数
if number%3 ==2 and number%5 ==3 and number%7 ==2:
    print(number,"符合条件：三三数之剩二，五五数之剩三，七七数之剩二")
else:
    print(number,"不符合条件")



# 输入年龄判断
print("\n 2、输入年龄判断")
your_age = int(input("请输入您的年龄：")) 
if your_age <= 18:          # 调用if语句判断输入的数据是否小于等于18
    # 如果小于等于18则输出提示信息
    print("您的年龄还小，要努力学习哦！")
elif 18 < your_age <= 30:    # 判断是否大于18岁，并且小于30岁
    # 如果输入的年龄大于18岁并且小于30岁则输出提示信息
    print("您现在的阶段正是努力奋斗的黄金阶段！")
elif 30 < your_age <= 50:     # 判断输入的年龄是否大于30岁小于等于50岁
    # 如果输入的年龄大于30岁而小于等于50岁则输出提示信息
    print("您现在的阶段正是人生的黄金阶段！")
else:
    print("最美不过夕阳红！")


# 判断输入的年份是不是闰年
print("3、判断输入的年份是不是闰年")
year = int(input("请输入一个年份："))   # 获取用户输入的年份，并转换为整型
if year % 4 == 0:                      # 四年一闰
    if year % 100 == 0:
        if year % 400 == 0:            # 四百年再闰
           print(year,"年是闰年")
        else:                           # 百年不闰
            print(year,"年不是闰年")
    else:
        print(year,"年是闰年")
else:
    print(year,"年不是闰年")




# while循环解决数学题
print("\n 今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？")
print("4.1、while循环版")
flag = True 
number = 0                                            
while flag:
    number += 1                                            
    if number%3 ==2 and number%5 ==3 and number%7 ==2:  
        print("答曰：这个数是",number)                    
        flag = False


# for循环解决数学题1
print("4.2、for循环版")
for i in range(100):
    if i%3 == 2 and i%5 == 3 and i%7 ==2 :
        print("这个数是：",i)
        

# for循环解决数学题2
print("4.3、for循环版改进版")
for i in range(100):
    if i%3 == 2 and i%5 == 3 and i%7 ==2 :
        print("这个数是：",i)
        break

# 打印九九乘法表
print("\n 5、打印九九乘法表")
for i in range(1,10): 		# 输出9行
    for j in range(1, i + 1):  	# 输出与行数相等的列
        print(str(j) + "×" + str(i) + "=" + str(i * j) + "\t",end = '')
    print("")	                # 换行


# 计算10以内(不包括10)所有偶数的和
total = 0
for i in range(1,10):
    if i%2 == 0:
        total += i
        print(i)
print("10以内(不包括10)所有偶数的和为：",total)















