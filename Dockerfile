# Python公式イメージを使用
FROM python:3.11

# 作業ディレクトリを作成
WORKDIR /code

# 依存ファイルをコピー＆インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトコードを追加
COPY . .

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
