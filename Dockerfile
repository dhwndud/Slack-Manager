FROM python:3.11.3-slim-buster as builder
COPY requirements.txt /build/
WORKDIR /build/
# 'WORKDIR' = 을 지정하면 그 이후 명령어는 컨테이너에서 해당 디렉토리를 기준으로 동작한다.
RUN pip install -U pip && pip install -r requirements.txt

FROM python:3.11.3-slim-buster as app
WORKDIR /app/
COPY *.py /app/
# 'COPY' = 호스트 시스템의 파일/디렉토리를 이미지에 복사한다.
RUN mkdir /app/app/
COPY app/*.py /app/app/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/ /usr/local/lib/
ENTRYPOINT python main.py
# 'ENTRYPOINT' = 이미지를 컨테이너로 실행시킬 때, 항상 실행되는 명령어를 지정

# docker build . -t your-repo/chat-gpt-in-slack
# export SLACK_APP_TOKEN=xapp-...
# export SLACK_BOT_TOKEN=xoxb-...
# export OPENAI_API_KEY=sk-...
# docker run -e SLACK_APP_TOKEN=$SLACK_APP_TOKEN -e SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN -e OPENAI_API_KEY=$OPENAI_API_KEY -it your-repo/chat-gpt-in-slack
