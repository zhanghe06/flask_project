FROM python:2.7.12
MAINTAINER zh "zhang_he06@163.com"

RUN apt-get update && apt-get install -qy --no-install-recommends \
    build-essential \
    apt-utils \
    python-dev \
    openssh-server \
    libmariadbd-dev \
    vim \
    ntpdate

ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 9001

WORKDIR /flask_project

#ENTRYPOINT ["supervisord"]
