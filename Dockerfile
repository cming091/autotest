FROM python:3.7.7
WORKDIR /data
COPY ./requirements.txt /data/
# RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#      && pip3 install -r /data/requirements.txt \
#      && apk del .build-deps gcc musl-dev
RUN pip3 install -r /data/requirements.txt
