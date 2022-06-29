FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt nltkdl.py /code/
RUN pip install -r requirements.txt
RUN python3 nltkdl.py
