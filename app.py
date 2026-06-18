from flask import Flask

app = Flask(__name__)

@app.route("/users")
def users():
    return {
        "users": ["alice", "bob"]
    }

app.run(host="0.0.0.0", port=5000)