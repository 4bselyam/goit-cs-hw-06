FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000
EXPOSE 5555

CMD ["sh", "-c", "python app.py & python socket_server.py"]