import random


names_text = input("请输入多个名字，并用英文逗号分隔：")
names = names_text.split(",")

selected_name = random.choice(names).strip()

print("本次抽中：" + selected_name)
