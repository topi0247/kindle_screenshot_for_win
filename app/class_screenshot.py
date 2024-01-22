import tkinter as tk
from tkinter import filedialog
import AppKit
import os
import time
import glob
import pyautogui
import shutil
from pathlib import Path
import img2pdf
import sys
from tkinter import  messagebox
from class_coordinate import Coordinate

class InvalidInputError(Exception):
  pass

class Screenshot:
  def __init__(self, master, label_L, label_R):
    self.master = master
    self.coord_L = Coordinate(master, label_L)
    self.coord_R = Coordinate(master, label_R)

  def browsefunc(save_dir_entry):
    filename = filedialog.askdirectory()
    save_dir_entry.delete(0, tk.END)
    save_dir_entry.insert(tk.END, filename)

  def extract_coordinates(text):
    # ラベルのテキストから座標だけを抽出する関数
      coords = text.split('=')[1].strip()
      x, y = map(int, coords.strip('()').split(','))
      return x, y

  def before_screenshot(title, save_dir, repetition, upper_left_label, lower_right_label):

    # ここ、｢クソコードだ｣って怒られそう
    # すべて突破したらスクショにうつるよ
    if upper_left_label == "" or lower_right_label == "":
      raise InvalidInputError("座標を設定してください")
    else :
      upper_left_coords = Screenshot.extract_coordinates(upper_left_label)
      lower_right_coords = Screenshot.extract_coordinates(lower_right_label)

      if title == "" or save_dir == "" :
        raise InvalidInputError("タイトルの入力または保存先の設定をしてください")
      else:
        if not repetition.isdigit() or int(repetition) <= 0:
          raise InvalidInputError("ページ数の欄には自然数を入力してください")
        else:
          return upper_left_coords, lower_right_coords

  def screenshot(title, save_dir, page_direction, repetition, upper_left_label, lower_right_label, title_entry):
    
    upper_left_coords, lower_right_coords = Screenshot.before_screenshot(title, save_dir, repetition, upper_left_label, lower_right_label)
    if upper_left_coords is None or lower_right_coords is None:
      return  # 必要な座標が取得できない場合は処理を中断
    
    # Kindle のウィンドウを探す
    all_windows = AppKit.NSWorkspace.sharedWorkspace().runningApplications()
    # 一致するウィンドウを変数に格納する
    for window in all_windows:
      if window.localizedName() == 'Kindle':
        kindle = window
        break
    else:
      raise InvalidInputError("Kinldeのウィンドウが見つかりませんでした。")

    os.makedirs(f'{save_dir}/{title}', exist_ok=True)

    #
    print(title)
    print("スクショ中...")
    #
    
    upper_left_x = upper_left_coords[0]
    upper_left_y = upper_left_coords[1]
    lower_right_x = lower_right_coords[0]
    lower_right_y = lower_right_coords[1]

    prev_screenshot = None
    for i in range(int(repetition)):
      # ウィンドウハンドルをkindleにわたす
      kindle.activateWithOptions_(AppKit.NSApplicationActivateIgnoringOtherApps)
      # スクショを撮る
      screenshot = pyautogui.screenshot(region=(upper_left_x, upper_left_y,
                                                lower_right_x-upper_left_x, lower_right_y-upper_left_y))
      screenshot.save(f'{save_dir}/{title}/{title}_{i}.png', "PNG")

      # ページを捲る
      if page_direction == 'right':
        pyautogui.press('right')
      else:
        pyautogui.press('left')
      
      # 同一ページをスクショしたら停止する。
      if prev_screenshot is not None:
        width, height =screenshot.size
        screenshot_rgb = [screenshot.getpixel((x, y)) for x in range(width) for y in range(height)]
        prev_screenshot_rgb = [prev_screenshot.getpixel((x, y)) for x in range(width) for y in range(height)]
        if screenshot_rgb == prev_screenshot_rgb:
          print('同一ページを検出')
          os.remove(f'{save_dir}/{title}/{title}_{i}.png')
          os.remove(f'{save_dir}/{title}/{title}_{i-1}.png')
          os.remove(f'{save_dir}/{title}/{title}_{i-2}.png')
          break
      prev_screenshot = screenshot
      time.sleep(0.3)
      
    ConvertToPDF.convert(save_dir, title, title_entry) # title_entry は main.py のエントリーボックスの参照

class ConvertToPDF:
  def convert(save_dir, title, title_entry):
    png_files = glob.glob(f'{save_dir}/{title}/*.png') # PNGファイルの検索、並べ替え
    png_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1]))
    png_data = [open(file, 'rb').read() for file in png_files]   # PNGファイルの読み込み
    
    # 標準エラー出力を一時的に置き換える
    original_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

    try:
      print("PDFに変換中...")
      with open(f'{save_dir}/{title}/{title}.pdf', 'wb') as f:  # PDFファイルの作成と保存
        f.write(img2pdf.convert(png_data))
    finally:
      # 標準エラー出力をもとに戻す
      sys.stderr.close()
      sys.stderr = original_stderr

    # 上記のように、try: finally で標準エラーを書き換えないと、
    # Image contains an alpha channel. Computing a separate soft mask (/SMask) image to store transparency in PDF.
    # が大量発生してしまう。
    # ただし、エラーメッセージを完全に無視することになるので、何か問題が発生した場合にそれを検知することができなくなる点には注意する

    shutil.move(f'{save_dir}/{title}/{title}.pdf', f'{save_dir}')  # PDFファイルの移動
    print("PDF化まで完了したんだナ\n")
    
    response = messagebox.showinfo("オワタ", "???｢PDF化まで完了したんだナ｣ ")
    if response == "ok":
      title_entry.delete(0, tk.END)

    if os.path.exists(f'{save_dir}/{title}'):  # 一時ディレクトリの削除
      shutil.rmtree(f'{save_dir}/{title}')     # ファイルを移動させる

if __name__ == "__main__":
  response = messagebox.showinfo("オワタ", "???｢このファイルは\nインポート専用なんだナ｣")
  if response == "ok":
    response2 = messagebox.showinfo("messagebox", "メッセージボックスのokボタンを...押したね??")
  if response2 == "ok":
    for i in range(47):
      izanami = messagebox.showinfo("uchiha", "イザナミだッ!!!")
    if izanami == "ok":
      messagebox.showwarning("aori", "よくここまで\nokボタン押し続けたね。\n\nえ、何?\n暇なの??\n\n")