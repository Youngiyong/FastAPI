# pull official base image
FROM python:3.7.7

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN apt-get update

RUN python --version
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
#RUN pip install --upgrade pip
#
#RUN pip install -r requirements.txt
RUN /bin/bash -c "source /venv/bin/activate; pip install -r requirements.txt"
RUN ls -l /venv/bin/
RUN source /venv/bin/activate

# copy project
COPY . /usr/src/app/
