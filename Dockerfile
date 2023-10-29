FROM python:3.8

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 8000
ENV APP_PREFIX = "/api"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
