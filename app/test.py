import pygetwindow as gw
import pyautogui
import time

# Kindleウィンドウのタイトルを指定
kindle_window_title = "Kindle"

# 指定したタイトルを含むウィンドウを取得
windows = gw.getWindowsWithTitle(kindle_window_title)
kindle_window = None
for window in windows:
    if kindle_window_title in window.title:
        kindle_window = window
        break

# Kindleウィンドウが見つかった場合
if kindle_window:
    # ウィンドウをアクティブにする
    kindle_window.activate()
    time.sleep(1)  # ウィンドウがアクティブになるのを少し待つ
    
    # 矢印キーを使ってページをめくる
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
else:
    print(f"'{kindle_window_title}' タイトルのウィンドウが見つかりませんでした。")