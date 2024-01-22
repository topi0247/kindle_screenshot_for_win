FROM python:3.11.7

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 依存関係ファイルをコピー
COPY requirements.txt ./

# 依存関係をインストール
RUN pip3 install --no-cache-dir -r requirements.txt

# プロジェクトファイルをコピー
COPY . .

# コンテナ起動時にPythonスクリプトを実行
CMD ["python", "./main.py"]
