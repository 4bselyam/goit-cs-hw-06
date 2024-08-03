import socket
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://admin:password@mongo:27017/")
db = client["message_db"]
collection = db["messages"]


def save_to_db(data):
    username, message = data.split(":")
    document = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "username": username,
        "message": message,
    }
    collection.insert_one(document)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5555))
    server_socket.listen(5)
    print("Socket server started on port 5555")

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024).decode("utf-8")
        save_to_db(data)
        client_socket.close()


if __name__ == "__main__":
    start_server()
