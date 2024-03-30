from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('temp1.html')

if __name__ == '__main__':
    app.run()

# $ python app.py
