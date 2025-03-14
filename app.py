import os
from flask import Flask

app = Flask(__name__)

# Load variables from Railway
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret-key')
TOKEN_EXPIRY = int(os.getenv('TOKEN_EXPIRY', 3600))

@app.route("/")
def home():
    return "Flask API is running!"

if __name__ == "__main__":
    app.run()
