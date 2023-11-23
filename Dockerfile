FROM python:3.10

ENV DockerHOME = /home/github/cubes1

RUN mkdir -p ${DockerHOME}

WORKDIR ${DockerHOME}

RUN python -m venv ./
RUN source bin/activate
RUN pip install -r requirements.txt

EXPOSE 7000

RUN python manage.py runserver 7000