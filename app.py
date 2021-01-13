from flask import Flask
import os

basedir = os.getcwd()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/dev.db"

@app.route("/api")
def api_home():
    return "API is working please add routes"

if __name__ == "__main__":
    app.run(host="192.168.1.2", port=80)