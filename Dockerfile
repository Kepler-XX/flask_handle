# 指定所创建镜像的基础镜像
FROM python:3.7

WORKDIR /var/www/flask_handle
COPY requirements.txt config.py run.py ./
COPY api ./api

#安装python依赖包
RUN apt-get update
RUN pip3 install -i https://pypi.doubanio.com/simple/ --upgrade pip
RUN pip3 install -i https://pypi.doubanio.com/simple/ -r requirements.txt

ENV LANG C.UTF-8

# 声明镜像内服务监听的端口
EXPOSE 3000