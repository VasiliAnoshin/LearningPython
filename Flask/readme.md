Initializing the app
app = Flask(__name__) sets the name of your app to the name of your module ("app" if "app.py" is the name of your file).

Using @app.route
@app.route('/')
def index():
  ...
In this case, @app.route is a Python decorator. 
Decorators take functions and returns another function, usually extending the input function with additional ("decorated") functionality.
@app.route is a decorator that takes an input function index() as the callback that gets invoked when a request to route / comes in from a client.

We run a flask app defined at app.py with FLASK_APP=app.py flask run
FLASK_APP must be set to the server file path with an equal sign in between. No spaces. 
FLASK_APP = app.py will not work. These flags have to be set exactly as expected, as FLAG=value.
To enable live reload, set export FLASK_ENV=development in your terminal session to enable debug mode, prior to running flask run. Or call it together with flask run:
$ FLASK_APP=app.py FLASK_DEBUG=true flask run