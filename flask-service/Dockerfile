FROM python:3.9

COPY . /web
WORKDIR /web

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]