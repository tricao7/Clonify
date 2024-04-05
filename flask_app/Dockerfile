FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update -qq && \
apt-get install -y --no-install-recommends \
libmpc-dev \
libgmp-dev \
libmpfr-dev

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]