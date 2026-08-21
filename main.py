import random
import tkinter as tk
from tkinter import messagebox


def draw_student():
    """从输入的学生姓名中随机抽取一人。"""
    names_text = names_input.get("1.0", tk.END)
    names = []

    for name in names_text.split(","):
        if name.strip():
            names.append(name.strip())

    if not names:
        messagebox.showinfo("提示", "请先输入学生姓名！")
        return

    selected_name = random.choice(names)
    result_label.config(text="本次抽中：" + selected_name)


window = tk.Tk()
window.title("学生随机抽签器 V3.0")
window.geometry("600x420")

tip_label = tk.Label(
    window,
    text="请输入学生姓名，并用英文逗号分隔：",
    font=("Microsoft YaHei", 13),
)
tip_label.pack(pady=(25, 10))

names_input = tk.Text(window, width=55, height=10, font=("Microsoft YaHei", 12))
names_input.pack(padx=25)

draw_button = tk.Button(
    window,
    text="开始抽签",
    font=("Microsoft YaHei", 13),
    command=draw_student,
)
draw_button.pack(pady=18)

result_label = tk.Label(
    window,
    text="等待抽签",
    font=("Microsoft YaHei", 20, "bold"),
    fg="#d9534f",
)
result_label.pack()

window.mainloop()
