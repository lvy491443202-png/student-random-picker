import random


print("欢迎使用学生随机抽签器 V2！")
names_text = input("请输入学生姓名，并用英文逗号分隔：")

names = []
for name in names_text.split(","):
    if name.strip():
        names.append(name.strip())

if names:
    selected_name = random.choice(names)
    print("本次抽中：" + selected_name)
else:
    print("没有输入学生姓名，请重新运行程序。")

input("按回车键退出...")
