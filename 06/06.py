# 字典：键值对key:value
# 1、字典的生成，利用dictionary = dict(zip(name,sign))转换为字典
print("1、字典的生成，利用dictionary = dict(zip(name,sign))转换为字典")
name = ['绮梦','冷伊一','香凝','黛兰']        # 作为键的列表
sign = ['水瓶座','射手座','双鱼座','双子座']  # 作为值的列表
dictionary = dict(zip(name,sign))# 转换为字典
print(dictionary)                              # 输出转换后字典

# 2、字典value的获取dictionary.get("key")
print("\n 2、字典value的获取get(key)")
name = ['绮梦','冷伊一','香凝','黛兰']        # 作为键的列表
sign_person = ['水瓶座','射手座','双鱼座','双子座']  # 作为值的列表
person_dict = dict(zip(name,sign_person))            # 转换为个人字典

sign_all =['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']
nature = ['有一种让人看见就觉得开心的感觉，阳光、乐观、坚强，性格直来直往，就是有点小脾气。',
          '很保守，喜欢稳定，一旦有什么变动就会觉得心里不踏实，性格比较慢热，是个理财高手。',
          '喜欢追求新鲜感，有点小聪明，耐心不够，因你的可爱性格会让很多人喜欢和你做朋友。',
          '情绪容易敏感，缺乏安全感，做事情有坚持到底的毅力，为人重情重义，对朋友和家人特别忠实。',
          '有着宏伟的理想，总想靠自己的努力成为人上人，向往高高在上的优越感，也期待被仰慕被崇拜的感觉。',
          '坚持追求自己的完美主义者。',
          '追求平等、和谐，擅于察言观色，交际能力很强，因此真心的朋友不少。最大的缺点就是面对选择总是犹豫不决。',
          '精力旺盛，占有欲强，对于生活很有目标，不达目的誓不罢休，复仇心重。',
          '崇尚自由，勇敢、果断、独立，身上有一股勇往直前的劲儿，只要想做，就能做。',
          '是最有耐心的，为事最小心，也是最善良的星座。做事脚踏实地，也比较固执，不达目的不放手，而且非常勤奋。',
          '人很聪明，最大的特点是创新，追求独一无二的生活，个人主义色彩很浓重的星座。',
          '集所有星座的优缺点于一身。最大的优点是有一颗善良的心，愿意帮助别人。']
sign_dict = dict(zip(sign_all,nature))# 转换为星座字典

print("【香凝】的星座是",person_dict.get("香凝"))      # 输出星座
print("她的性格特点是：\n\n",sign_dict.get(person_dict.get("香凝")))  # 输出性格特点

# 3、用列表推导式生成字典
print("\n 3、用列表推导式生成字典")
name = ['绮梦','冷伊一','香凝','黛兰'] 
sign = ['水瓶','射手','双鱼','双子'] 
dictionary = {i:j+'座' for i,j in zip(name,sign)}# 使用列表推导式生成字典
print(dictionary)        



# 4、字典的输出
print("\n ")
python = {'绮梦','冷伊一','香凝','梓轩'}
print('选择Python语言的学生有：',python,'\n')
c = {'冷伊一','零语','梓轩','圣博'}
print('选择C语言的学生有：',c)

# 方法二：
print("\n ")
python = set(['绮梦','冷伊一','香凝','梓轩'])       # 保存选择Python语言的学生名字
print('选择Python语言的学生有：',python,'\n')       # 输出选择Python语言的学生名字
c = set(['冷伊一','零语','梓轩','圣博'])  # 保存选择C语言的学生名字
print('选择C语言的学生有：',c)       # 输出选择C语言的学生名字

# 5、字典的添加add和删除remove
python = set(['绮梦','冷伊一','香凝','梓轩'])       # 保存选择Python语言的学生名字
python.add('零语')                                  # 添加一个元素
print('选择Python语言的学生有：',python,'\n')       # 输出选择Python语言的学生名字
c = set(['冷伊一','零语','梓轩','圣博'])  # 保存选择C语言的学生名字
c.remove('零语')                     # 删除指定元素
print('选择C语言的学生有：',c)       # 输出选择C语言的学生名字


# 6、字典集合的运算
python = set(['绮梦','冷伊一','香凝','梓轩'])       # 保存选择Python语言的学生名字
c = set(['冷伊一','零语','梓轩','圣博'])             # 保存选择C语言的学生名字
print('选择Python语言的学生有：',python)            # 输出选择Python语言的学生名字
print('选择C语言的学生有：',c)      # 输出选择C语言的学生名字
print('交集运算：',python & c)      # 输出既选择了Python语言又选择C语言的学生名字
print('并集运算：',python | c)      # 输出参与选课的全部学生名字
print('差集运算：',python - c)      # 输出选择了Python语言但没有选择C语言的学生名字


