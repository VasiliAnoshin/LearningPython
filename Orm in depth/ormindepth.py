from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user@localhost:5432/jane'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

  def __repr__(self):
      return f'<User {self.id}, {self.name}>'

db.create_all()
print(Person.query.all())

#Implement a query to filter all users by name 'Bob'.
res = Person.query.filter_by(name='Bob').all()
print(res)
#Implement a LIKE query to filter the users for records with a name that includes the letter "b".
res = Person.query.filter(Person.name.like('%b%')).all()
print(res)
#Return only the first 5 records of the query above.
res = Person.query.limit(5).all()
print(res)
#Re-implement the LIKE query using case-insensitive search.
res = Person.query.filter(Person.name.ilike('%b%')).all()
print(res)
#Return the number of records of users with name 'Bob'.
res = Person.query.filter(Person.name.ilike('%b%')).count()
print(res)
