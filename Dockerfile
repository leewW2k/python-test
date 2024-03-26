FROM python:3.11-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main:ApiClient", "--proxy-headers", "--host", "localhost", "--port", "8888"]
