FROM ubuntu:16.04

RUN apt update
RUN apt-get install -y locales python3-pip python3-dev python3-virtualenv fabric \
      libpq-dev libjpeg-dev libxml2-dev libxslt-dev libfreetype6-dev libffi-dev \
      postgresql-client git curl wget
RUN pip3 install jsonschema
RUN pip3 install urllib3
RUN mkdir /hotel
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

#ADD . /hotel
ADD entry_point.sh /

CMD ./entry_point.sh
