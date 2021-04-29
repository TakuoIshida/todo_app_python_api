FROM python:3.8 AS builder

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

# --system: 仮想環境を作成せず直接installする
# --deploy を付けると、PipfileとPipfile.lock にズレがあるとき（pipenv syncし忘れた時）に、エラーにします。（本番環境用設定）
RUN pip install pipenv \
  && pipenv install --system

ENV PYTHONUNBUFFERED=1

FROM python:3.8-slim

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

COPY . ./