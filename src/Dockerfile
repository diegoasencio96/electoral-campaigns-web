FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install gdal-bin -y
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh