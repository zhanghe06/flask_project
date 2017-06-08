FROM python:2.7.13
MAINTAINER zh "zhang_he06@163.com"

RUN echo "deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib\n" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib\n" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib\n" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib\n" >> /etc/apt/sources.list \
    && mkdir -p ~/.pip/ \
    && echo "[global]\n" > ~/.pip/pip.conf \
    && echo "index-url = http://mirrors.aliyun.com/pypi/simple/\n\n" >> ~/.pip/pip.conf \
    && echo "[install]\n" >> ~/.pip/pip.conf \
    && echo "trusted-host=mirrors.aliyun.com\n" >> ~/.pip/pip.conf

RUN apt-get update && apt-get install -qy --no-install-recommends \
    build-essential \
    apt-utils \
    python-dev \
    openssh-server \
    libmariadbd-dev \
    vim \
    ntpdate \
    net-tools

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt && rm -f /requirements.txt

#RUN pip install --no-cache-dir \
#    Flask \
#    Flask-Login \
#    Flask-Mail \
#    Flask-SQLAlchemy \
#    Flask-WTF \
#    Flask-OAuthlib \
#    Flask-Excel \
#    Flask-Moment \
#    Flask-Uploads \
#    Flask-Principal \
#    sqlacodegen \
#    gunicorn \
#    schedule \
#    supervisor \
#    redis \
#    requests \
#    celery \
#    librabbitmq \
#    pika \
#    Pillow \
#    sshtunnel \
#    MySQL-python \
#    pymongo


EXPOSE 9001 8000 8010

WORKDIR /flask_project

#ENTRYPOINT ["supervisord"]
