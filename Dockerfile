FROM python:3.10.11-buster
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
