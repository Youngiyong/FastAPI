# pull official base image
FROM python:3.7.7

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

RUN python --version
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip install --upgrade pip

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# copy project
COPY . /usr/src/app/

RUN python3 -m venv venv
RUN ls -al
RUN . venv/bin/activate && pip install -r requirements.txt
RUN ls -al venv/
