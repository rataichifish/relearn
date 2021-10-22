
year = 2020   # 年份
result = "是闰年" if (year%4==0 and year % 100 !=0) or (year%100 == 0) else "不是闰年"
print("\n"+str(year) + "年" + result + "!")  # 输出结果

print("面包店正在打折，活动进行中……")                             # 输出提示信息
strWeek = input("请输入中文星期（如星期一）：")                     # 输入星期，例如，星期一
intTime = int(input("请输入时间中的小时（范围：0~23）："))          # 输入时间，由于input()方法返回的结果为字符串类型，所以需要进行类型转换
# 判断是否满足活动参与条件（使用了if条件语句)
if (strWeek == "星期二" and  (intTime >= 19 and intTime <= 20)) or (strWeek == "星期六" and (intTime >= 17 and intTime <= 18)):
    print("恭喜您，获得了折扣活动参与资格，尽情选购吧！")           # 输出提示信息
else:
    print("对不起，您来晚一步，期待下次活动……")                   # 输出提示信息




python = 95                          # 定义变量，存储python的分数
english = 92                         # 定义变量，存储english的分数
c = 89                               # 定义变量，存储C语言的分数
# 输出3个变量的值
print("python = " + str(python) + "english = " +str(english) + "c = " +str(c) + "\n")
print("python < english的结果：" + str(python < english))    # 小于操作
print("python > english的结果：" + str(python > english))    # 大于操作
print("python == english的结果：" + str(python == english))  #　等于操作
print("python != english的结果：" + str(python != english))  # 不等于操作
print("python <= english的结果：" + str(python <= english))  # 小于等于操作
print("english >= c的结果：" + str(python >= c))  # 大于等于操作



python = 95                          # 定义变量，存储Python的分数
english = 92                         # 定义变量，存储English的分数
c = 89                               # 定义变量，存储C语言的分数
sub = python - c                     # 计算Python和C语言的分数差
avg = (python + english + c) / 3     # 计算平均成绩
print("Python课程和C语言课程的分数之差： " + str(sub) + " 分\n")
print("3门课的平均分： " + str(avg) + " 分")





password = 87654321   # 密码
key = 7 # 加密参数
print("\n原密码：",password)  # 输出原密码
password = password << key  # 将原密码左移，生成新的数字
print("\n加密后：",password)  # 输出加密后的密码
password = password >> key  # 将新密码右移，还原密码
print("\n解密后：",password)  # 输出解密后的密码

