FROM python:latest

WORKDIR /src

COPY requirement.txt /src/

RUN pip install -r requirements.txt

COPY . /src/

EXPOSE 8000

CMD ["gunicorn","A.wsgi",":8000"]
