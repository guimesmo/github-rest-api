FROM python:3-alpine

WORKDIR /usr/src/
RUN apk add python3-dev build-base linux-headers pcre-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY application .
COPY deployments .

CMD [ "make", "runserver" ]
