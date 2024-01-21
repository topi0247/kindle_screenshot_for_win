import tkinter as tk
from class_coordinate import Coordinate
from class_screenshot import Screenshot

if __name__ == "__main__":
  
  # GUIの作成
  root = tk.Tk()
  root.geometry('400x230')
  root.title('Kindle Screenshot App')
  frame = tk.Frame(root)
  frame.pack()
  
  # タイトル入力する
  title_label = tk.Label(frame, text='タイトル:')
  title_entry = tk.Entry(frame)

  title_label.grid(row=0, column=0)
  title_entry.grid(row=0, column=1)

  # 保存場所用テキストボックスを設置する
  save_dir_label = tk.Label(frame, text='保存先:')
  save_dir_entry = tk.Entry(frame)

  # 保存先を設定 (クラスメソッドに参照渡し)
  browsebutton = tk.Button(frame, text="参照", command=lambda: Screenshot.browsefunc(save_dir_entry))
  browsebutton.grid(row=1, column=2, columnspan=2)

  save_dir_label.grid(row=1, column=0)
  save_dir_entry.grid(row=1, column=1)

  # ページめくり方向選択する
  direction_label = tk.Label(frame, text='ページの捲る方向:')

  direction_var = tk.StringVar(value='right')
  direction_radiobutton1 = tk.Radiobutton(frame, text='左', variable=direction_var, value='left')
  direction_radiobutton2 = tk.Radiobutton(frame, text='右', variable=direction_var, value='right')
  
  direction_label.grid(row=2, column=0)
  direction_radiobutton1.grid(row=2, column=0, columnspan=3)
  direction_radiobutton2.grid(row=2, column=1, columnspan=2)

  # ページめくり回数を入力する
  repetition_label = tk.Label(frame, text='ページ数:')
  repetition_entry = tk.Entry(frame)
  
  repetition_entry.insert(0, "2000")
  
  repetition_label.grid(row=3, column=0)
  repetition_entry.grid(row=3, column=1)

  # 座標を表示する
  upper_left_label = tk.Label(frame, text='', anchor='w')
  lower_right_label = tk.Label(frame, text='', anchor='w')
  
  upper_left_label.grid(row=4, column=1, columnspan=3,sticky='w', padx=(75, 0))
  lower_right_label.grid(row=5, column=1, columnspan=5, sticky='w', padx=(75, 0))
  
  # 座標をインスタンス化する 
  coord_L = Coordinate(root, upper_left_label)
  coord_R = Coordinate(root, lower_right_label)
  
  # 座標を決めるボタン
  select_R_button = tk.Button(frame, text="左上", command=lambda:coord_L.start_tracking())
  select_L_button = tk.Button(frame, text="右下", command=lambda:coord_R.start_tracking())
  
  select_R_button.grid(row=4, column=0, columnspan=2)
  select_L_button.grid(row=5, column=0, columnspan=2)
  
  set_coord_label = tk.Label(frame, text="座標を設定:")
  how_to_use = tk.Label(frame, text="(ボタンを押した後\nカーソルをあわせて\nescキーを押す)")
  
  set_coord_label.grid(row=4, rowspan=1, column=0)
  how_to_use.grid(row=5, rowspan=1, column=0)

  screenshot_button = tk.Button(frame,
                                text='スクショしてPDFにする', 
                                command=lambda: 
                                Screenshot.screenshot(
                                                      title_entry.get(),
                                                      save_dir_entry.get(),
                                                      direction_var.get(),
                                                      repetition_entry.get(),
                                                      upper_left_label.cget("text"),
                                                      lower_right_label.cget("text"),
                                                      title_entry  # 参照渡し
                                                      ))
  screenshot_button.grid(row=10, rowspan=3, column=1)

  root.mainloop()