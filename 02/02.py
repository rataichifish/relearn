# BMI指数
print("1、输出自己的BMI指数")
height = 1.73     # 保存身高的变量，单位：米
print("您的身高：" + str(height))
weight = 61      # 保存体重的变量，单位：千克
print("您的体重：" + str(weight))
bmi=weight/(height*height)      # 用于计算BMI指数，公式为“体重/身高的平方”
print("您的BMI指数为："+str(bmi))  #输出BMI指数
            # 判断身材是否合理
if bmi<18.5:
    print("您的体重过轻 ~@_@~")
if bmi>=18.5 and bmi<24.9:
    print("正常范围，注意保持 (-_-)")
if bmi>=24.9 and bmi<29.9:
    print("您的体重过重 ~@_@~")
if bmi>=29.9:
    print("肥胖 ^@_@^")



# 输出一幅图
print("\n 2、输出一幅图")
print('''
                       ▶  学编程，你不是一个人在战斗~~
                       |                   
                __\--__|_ 
II=======OOOOO[/ ★007___|           
          _____\______|/-----. 
        /___mingrisoft.com___|              
         \◎◎◎◎◎◎◎◎⊙/ 
           ~~~~~~~~~~~~~~~~
''')


# 超市抹零（固定）
print("\n 3、超市抹零（固定）")
money_all = 56.7 + 72.9 + 88.5 + 26.6 + 68.8  # 累加总计金额
money_all_str = str(money_all)                # 转换为字符串
print("商品总金额为：" + money_all_str)
money_real = int(money_all)                   # 进行抹零处理
money_real_str = str(money_real)              # 转换为字符串
print("实收金额为：" + money_real_str)


# 超市抹零（根据输入抹零）
print("\n 4、超市抹零（根据输入抹零）")
all= 0
i = float(input("请输入金额："))
while(i != 0):
    all += i
    i = float(input("请输入金额(结束输入请输入0)："))
print("结束输入！\n 总计金额为：",all)
print("实收金额为：",int(all))


# BMI指数（输入型）
print("\n 5、输出BMI指数")
height = float(input("请输入您的身高（单位为米）："))      # 输入身高，单位：米
weight = float(input("请输入您的体重（单位为千克)："))     # 输入体重，单位：千克
bmi=weight/(height*height)      # 用于计算BMI指数，公式为“体重/身高的平方”
print("您的BMI指数为："+str(bmi))  # 输出BMI指数
# 判断身材是否合理
if bmi<18.5:
    print("您的体重过轻 ~@_@~")
if bmi>=18.5 and bmi<24.9:
    print("正常范围，注意保持 (-_-)")
if bmi>=24.9 and bmi<29.9:
    print("您的体重过重 ~@_@~")
if bmi>=29.9:
    print("肥胖 ^@_@^")


# practice 1
print("\n\n练习1：将输入的十进制整数转换为二进制、八进制和十六进制的数")

number = int(input('请输入一个十进制的整数：'))  # 输入一个十进制的数
b = bin(number)  # 转换为二进制数
o = oct(number)  # 转换为八进制数
h = hex(number)  # 转换为十六进制数
print('十进制数',number,'的二进制数为',b)
print('十进制数',number,'的八进制数为',o)
print('十进制数',number,'的十六进制数为',h)

# practice 2
print("\n\n 电影打分")
num=input("请您为《肖申克的救赎》这部电影打分（只能输入数字1~9）：")
print("您为《肖申克的救赎》电影的评价是",int(num)*"★")




