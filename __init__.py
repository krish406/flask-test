import os
#from flask class import Flask object
from flask import Flask

#function which sets up the website (application factory)
def create_app(test_config = None):
    #first parameter is the name of the current module used to set up paths
    #second parameter is saying that we are configuring relative to the instance folder
    app = Flask(__name__, instance_relative_config = True)
    #default configuration settings
    app.config.from_mapping(
        SECRET_KEY='dev',
        #add a file to flask-test folder, make database = to the path to the new file
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    return app