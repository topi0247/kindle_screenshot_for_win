# kindle_screenshot

※[kindle_screenshot](https://github.com/Dingu-suke/kindle_screenshot)をWindowsでできるようにしているものです

This is a code for taking screenshots of Kindle on Mac using Python for Japanese people.

これは、pythonのtkinterを学習するためのスクリプト集です。

【注意点】
appディレクトリ内のmain.pyがスクリーンショットするスクリプトとなっております。(classから始まる2つのファイルは、main.pyにインポートするクラスファイルとなっております)しかし、main.pyは残念ながらmacOSでしか動きません。というのも、class_screenshot.pyで使用しているAppKitというモジュールがmacOS専用であるためです。因みに、このモジュールはmacのウィンドウハンドルを取得するために使っております。macのKindleのウィンドウハンドルを取得するコードとなっており、ページをめくり、スクショを実行、これを繰り返します。ややこしいのですが、Kindle Classic という古い公式アプリもあります。今回使用するものはそちらではございません。"Kindle"です。App storeにてKindleと検索すれば見つかると思います。

Windowsの環境では、pywinautoのようなWindows専用のモジュールがあると思います。以前はWindowsのPCでスクショしていたので、実現はできるはずです。

Docker環境で作らない理由としては、DockerはLinuxベースであり、mac専用のモジュールが稼働できないからです。macの仮想環境をつくるDockerのようなものがあれば行けそうですが。現段階では取り組んでいません。

そのため、ローカル環境に落とし込んで使うかたちになります。
ローカル環境で使うには、モジュールをpip3コマンドを使用してインストールする必要があります。mac標準のpythonやpyenvなど、python環境によっても多少異なります。pip3コマンドはpythonバージョン3で使用し、pipコマンドはpythonバージョン2で使用します。
バージョンの確認方法は、以下のどちらかで確認することができます。

python3 --version 

python --version 

モジュールをインストールするコマンド例 (mac標準python)

pip3 install pyautogui

pip3 install appkit

pip3 install img2pdf

pip3 install pynput(sample/mouse_coordinate/mouse_coordinate.py 用)

モジュールが正しくインストールできていれば、main.pyを実行してkindleスクリーンショットのウィンドウが出てくるはずです。
その他にも何か問題がある場合は、コード的には正しい思いますので、環境関係の問題だと思います。
