from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return {'policy main endpoint': 'api is working!'}


if __name__ == '__main__':
    app.run()

