FROM python:3.11-alpine

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
