FROM ubuntu:18.04

COPY ./services /services
COPY ./models/trained /models/trained
COPY ./scripts /scripts

RUN ./scripts/install.sh

WORKDIR /services

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 9001

CMD python3 service.py