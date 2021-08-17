# create an application and run the application
from website import create_app
from flask_session import Session

app = create_app()
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# only run if you execute this file
if __name__ == '__main__': 
  app.run(debug=True) # stops us from re running flask all the time


  