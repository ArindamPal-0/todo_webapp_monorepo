from flask import Flask
from flask_cors import CORS
# import models.todos as todos_model
from models.todos import db, test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all(app=app)

# enabling cors for all sites
cors = CORS(app)

# testing route
@app.route('/')
def hello_world():
    return {'msg': 'Hello, World!'}


if __name__ == '__main__':
    # starting api server in debug mode
    # app.run(debug=True, host='0.0.0.0', port=5000)

    test(app)
    

    pass
