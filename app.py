from flask import Flask
from database import setup
from resources.tasks import task_bp
from flask_cors import CORS 

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
setup.create_tables()

@app.before_first_request
def create_tables():
  setup.create_tables()

app.register_blueprint(task_bp)

if __name__ == '__main__':
  app.run(debug=True, port=8000)