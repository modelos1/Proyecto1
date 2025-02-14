FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#COPY /backendpython/ .
#COPY /api_gateway/ .
COPY /backendpython/ .
COPY api_gateway /app/api_gateway
EXPOSE 8000 8001
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"& \
   # "uvicorn" "api_gateway.gateway:app", "--host", "0.0.0.0", "--port", "8001"]
CMD uvicorn main:app --host 0.0.0.0 --port 8000 & \
   uvicorn api_gateway.gateway:app --host 0.0.0.0 --port 8001

# docker build -t transactions_python_backend:0.0.1 .
# docker run -d -p 8001:8001 --name transactions_python_backend transactions_python_backend:0.0.1