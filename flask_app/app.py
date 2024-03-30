from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Voice Cloning App!'

if __name__ == '__main__':
    app.run()

# $ python app.py