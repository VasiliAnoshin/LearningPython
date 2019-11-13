from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#standart way for creating a flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER@localhost:5432/jane'
#TODO WHY IS THIS HERE ? https://github.com/pallets/flask-sqlalchemy/issues/351
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
db.create_all()

@app.route('/')
#index is a standart name for the route handler that listens for connections 
#to the root route and figures out what to do next
def index():
        person = Person.query.first()
        return 'Hello ' + person.name

# Alternative approach to run a Flask app: using __main__
if __name__ == "__main__":
    app.run()