import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # 1秒ごとに時刻を更新

root = tk.Tk()
root.title("Digital Clock")
root.geometry('350x150')

clock_label = tk.Label(root, font=('times', 50, 'bold'), bg='white')
clock_label.pack()

update_time()  # 時刻の更新を開始

root.mainloop()
