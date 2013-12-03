
from flask import Flask, send_file

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/<path>')
def index(path=None):
    if path:
        print path
        return send_file(path)
    else:
        return send_file('index.html')



if __name__ == '__main__':
    app.run()
