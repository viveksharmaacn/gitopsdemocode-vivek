from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello GitOps - Rakhi Parashar'

if __name__ == "__main__":
    app.run(debug=True)
