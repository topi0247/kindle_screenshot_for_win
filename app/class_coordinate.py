import pyautogui
import tkinter as tk

class Coordinate:
  def __init__(self, master, label_x_y):
    self.master = master
    self.coordinates_x_y= label_x_y
    self.coordinates = None

  def start_tracking(self):
    self.update_coordinates()
    # ESCキーのバインディング
    self.master.bind('<Escape>', self.stop_tracking)

  def update_coordinates(self):
    self.coordinates = pyautogui.position()
    # ここで繰り返し座標を更新する
    self.master.after(100, self.update_coordinates)  # 100ミリ秒ごとに更新

  def stop_tracking(self, event=None):
    # ESCキーが押されたときに実行される
    self.master.unbind('<Escape>')  # キーバインディングを解除
    if self.coordinates_x_y:
      x, y = self.coordinates 
      self.coordinates_x_y.config(text="(x, y) = {0}".format((x, y)))
    print("Captured Coordinates: {0}".format(self.coordinates))


# 挙動確認のためのTkinter
if __name__ == "__main__":
  # ボタンを押してからescキーを押すとマウスカーソルの座標がラベルに表示される
  root = tk.Tk()
  root.geometry("400x200")
  root.title("coordinate_test_window")

  how_to_use = tk.Label(root, text="Press the button, \n then press the esc key \n to display the coordinates.")
  sign = tk.Label(root, text="Captured Coordinates ▼")
  coordinates_x_y = tk.Label(root, text="")
  how_to_use.pack()

  mouse_coord = Coordinate(root, coordinates_x_y) # (インスタンス化)

  start_button = tk.Button(root, text='Start Tracking', command=mouse_coord.start_tracking)
  start_button.pack()
  sign.pack()
  coordinates_x_y.pack()

  root.mainloop()  # Tkinterのメインループを開始