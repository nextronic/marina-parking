FROM python:alpine


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev build-base linux-headers

RUN apk --no-cache add msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f

RUN apk add --no-cache jpeg-dev zlib-dev

RUN pip install Pillow

EXPOSE 1883
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


CMD  python3 app.py