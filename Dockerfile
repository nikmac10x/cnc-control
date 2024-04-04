FROM python:3.10

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app
COPY ./migrations /code/migrations
COPY yoyo* /code/

CMD ["uvicorn", "app.main:app", "--hostt=0.0.0.0", "--port=8000"]
