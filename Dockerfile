FROM python:3.6

COPY requirements.txt .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

RUN apt-get update && apt-get install -y tzdata

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/\$TZ /etc/localtime && echo \$TZ > /etc/timezone

WORKDIR /home/yx/Secure_login/


