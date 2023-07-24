FROM alpine:3.12

ADD main.py /app/main.py
COPY bin /app/bin

RUN apk add --no-cache python3 github-cli

ENTRYPOINT [ "/app/bin/entrypoint.sh" ]