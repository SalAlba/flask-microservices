# https://github.com/marcel-dempers/docker-development-youtube-series/blob/master/python/dockerfile
# https://runnable.com/docker/python/dockerize-your-flask-application

FROM python:3.6-alpine

ENV ENV_VARIABLE_FROM_DOCKER "Hello, World!"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY run_app.py run_app.py
COPY ./app /app


EXPOSE 2020
ENTRYPOINT ["python"]
CMD ["run_app.py"]