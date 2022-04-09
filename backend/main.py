from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# enabling cors for all sites
cors = CORS(app)

# testing route
@app.route('/')
def hello_world():
    return {'msg': 'Hello, World!'}


if __name__ == '__main__':
    # starting api server in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)