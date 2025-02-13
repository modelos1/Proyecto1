FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /backendpython/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t transactions_python_backend:0.0.1 .
# docker run -d -p 8000:8000 --name transactions_python_backend transactions_python_backend:0.0.1