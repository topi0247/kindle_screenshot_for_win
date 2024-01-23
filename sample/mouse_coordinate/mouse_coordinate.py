
# このクラスファイルはインポートしない

import tkinter as tk
from pynput import mouse
import threading

class MouseCoordinate:
  def __init__(self, label):
    self.coordinates = None
    self.stop_thread = threading.Event()
    self.label = label

  def start_coordinate_tracking(self):
    self.stop_thread.clear()
    listener_thread = threading.Thread(target=self.start_mouse_listener)
    listener_thread.start()

  def start_mouse_listener(self):
    with mouse.Listener(on_click=self.on_click) as listener:
      listener.join()

  def on_click(self, x, y, button, pressed):
    if pressed:
      x = round(x)
      y = round(y)
      self.coordinates = (x, y)
      self.label.config(text=f'Captured Coordinates: {self.coordinates}')
      return False  # Listenerを停止

if __name__ == "__main__":
  root = tk.Tk()
  root.title("Mouse Coordinate Tracker")
  root.geometry("300x150")

  coordinate_label = tk.Label(root, text="Press 'Start' \n and then click to capture coordinates")
  coordinate_label.pack()

  mouse_coord = MouseCoordinate(coordinate_label)

  start_button = tk.Button(root, text="Start Tracking", command=mouse_coord.start_coordinate_tracking)
  start_button.pack()

  root.mainloop()
