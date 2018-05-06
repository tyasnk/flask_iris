FROM python:3.6.5

RUN mkdir -p /usr/src/app /var/log/app /etc/app /model

WORKDIR /usr/src/app
VOLUME /var/log/app /etc/app /model

ENV APP_DEBUG=FALSE \
    APP_CONFIG_FILENAME=/etc/app/config.ini \
    APP_LOG_DIR=/var/log/app \
    APP_LOG_LEVEL=INFO \
    APP_MODEL_DIR=/model \
    APP_HOST=0.0.0.0 \
    APP_PORT=5000

EXPOSE 5000

COPY requirements.txt /usr/src/app

RUN pip3 install -r requirements.txt

COPY model/model.pkl /model

COPY . /usr/src/app

CMD ./start-gunicorn.sh
