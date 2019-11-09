from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#standart way for creating a flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER@localhost:5432/jane'
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
#index is a standart name for the route handler that listens for connections 
#to the root route and figures out what to do next
def index():
    return 'Hello World!'

# Alternative approach to run a Flask app: using __main__
if __name__ == "__main__":
    app.run()