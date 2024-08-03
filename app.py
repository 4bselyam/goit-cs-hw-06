from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
import socket
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]
        data = f"{username}:{message}".encode("utf-8")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 5555))
        sock.sendall(data)
        sock.close()

        return redirect(url_for("index"))
    return render_template("message.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
