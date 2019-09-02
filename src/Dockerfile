FROM python:3.7.4
MAINTAINER Diego A Asencio C <diegoasencio96@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install gdal-bin -y
RUN mkdir logs
VOLUME ["/logs/"]
ADD . /code/
RUN pip install -r /code/requirements.txt
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT ["/docker-entrypoint.sh"]