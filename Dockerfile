FROM ubuntu:latest
LABEL authors="maelb"

RUN apt-get update && apt-get install -y make

ENTRYPOINT ["top", "-b"]