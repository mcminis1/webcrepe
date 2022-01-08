FROM postgres:12.9

RUN apt-get update && apt-get install --yes postgresql-server-dev-12 python3-setuptools python3-dev make gcc git python3-pip
RUN git clone https://github.com/sawtoothdata/Multicorn.git 
RUN cd Multicorn && PYTHON_OVERRIDE=python3.9 make all install

WORKDIR /app
COPY . .

RUN apt-get install python3-pip -y
RUN python3.9 -m pip install --system multicorn requests .


USER postgres
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]