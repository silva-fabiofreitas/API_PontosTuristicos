FROM python:3.9.6-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY  requirements-dev.txt requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD [ "sh", "./entrypoint.sh" ]
