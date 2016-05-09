FROM centos
MAINTAINER Bruno Rocha <rochacbruno@gmail.com>

RUN yum update -y
RUN yum install -y libjpeg-devel tree git gcc python-devel zlib-devel openjpeg-devel python-imaging
RUN curl https://bootstrap.pypa.io/get-pip.py|python

COPY ./ /root/app/

WORKDIR /root/app/
RUN pip install -r requirements/requirements.txt
RUN pip install uwsgi

CMD uwsgi uwsgi.ini
