# kindle_screenshot

This is a code for taking screenshots of Kindle on Mac using Python for Japanese.

これは、pythonのtkinterを学習するためのスクリプト集です。

【注意点】
main.pyが、スクリーンショットするスクリプトですが、macOSでしか動きません。AppKitというモジュールがmacOS専用のためです。このモジュールは、ウィンドウハンドルを取得するために使います。
Windowsの環境では、確かpywinautoのようなmoduleがあったっけな。いずれにせよ、以前はwindowsのPCでスクショしていたので、実現はできるはずです。
Docker環境で作らない理由としては、DockerはLinuxベースであり、mac専用のmoduleが稼働できないからです。
macの仮想環境をつくるDockerのようなものがあれば行けそうですが。現段階では、それについて調べる、ということすらできてないですね。

local環境で使うには、moduleをpip3コマンドを使用してインストールする必要があります。mac標準のpythonやpyenvなど、python環境によっても多少異なります。pip3コマンドはpythonバージョン3で使用し、pipコマンドはpythonバージョン2で使用します。
バージョンの確認方法は、以下のどちらかで確認することができます。

python3 --version 
python --version 

モジュールをインストールするコマンド例 (mac標準python)
pip3 install pyautogui
pip3 install appkit
pip3 install img2pdf

pip3 install pynput

moduleが正しくインストールできていれば、main.pyを実行してkindleスクリーンショットのウィンドウが出てくるはずです。
その他にも何か問題がある場合は、コード的には正しい思いますので、環境関係の問題だと思います。