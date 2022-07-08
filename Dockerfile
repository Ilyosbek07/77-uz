FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# https://www.postgresql.org/download/linux/debian/
RUN echo "deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update \
    && apt-get install -y postgresql-client-12 \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir gunicorn gevent

COPY . /app/
WORKDIR /app/
