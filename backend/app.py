from flask import Flask, request
import os

app = Flask(__name__)

DATA_FOLDER = "/app/data"

os.makedirs(DATA_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/save", methods=["POST"])
def save_note():

    employee = request.form["employee"]
    note = request.form["note"]

    filename = f"{employee}.txt"

    filepath = os.path.join(DATA_FOLDER, filename)

    with open(filepath, "a") as file:
        file.write(note + "\n")

    return f"Note saved for {employee}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)