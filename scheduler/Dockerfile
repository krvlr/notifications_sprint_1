FROM python:3.10
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
COPY src .
ENTRYPOINT ["python", "main.py"]