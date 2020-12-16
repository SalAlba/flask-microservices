# https://github.com/marcel-dempers/docker-development-youtube-series/blob/master/python/dockerfile
# https://runnable.com/docker/python/dockerize-your-flask-application

FROM python:3.6-alpine

ENV ENV_VARIABLE_FROM_DOCKER "Hello, World!"

RUN mkdir /src
COPY ../requirements.txt /src/requirements.txt
COPY run_app.py /src/run_app.py
COPY ./app /src/app

WORKDIR /src
RUN pip install -r requirements.txt

EXPOSE 2020
ENTRYPOINT ["python"]
CMD ["run_app.py"]