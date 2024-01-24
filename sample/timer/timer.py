import tkinter as tk

def start_timer():
    try:
        # テキストボックスから時間を取得し、秒に変換
        time_in_min = float(entry.get())
        time_in_sec = int(time_in_min * 60)
        count_down(time_in_sec)
    except ValueError:
        # 数値以外が入力された場合
        timer_label.config(text="数字を入力して")
        return

def reset_timer():
    # タイマーをリセットし、ラベルを「00:00」に設定
    root.after_cancel(timer)
    timer_label.config(text="00:00")

def count_down(count):
    global timer  # グローバル変数として定義
    minutes = count // 60
    seconds = count % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        timer_label.config(text="終了！")

root = tk.Tk()
root.title("タイマー")

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="スタート", command=start_timer)
start_button.pack()

reset_button = tk.Button(root, text="リセット", command=reset_timer)
reset_button.pack()

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack()

root.mainloop()
