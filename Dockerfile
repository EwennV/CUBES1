FROM python:3.10

ENV DockerHOME = /home/cesi/cubes1

RUN mkdir -p ${DockerHOME}

WORKDIR ${DockerHOME}

COPY . ${DockerHOME}

RUN pip install -r requirements.txt

EXPOSE 7000

RUN python manage.py runserver 7000