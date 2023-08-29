from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

def plus(a, b):
    return a+b

if __name__ == '__main__':
    app.run()
    print(plus(3, 4))
