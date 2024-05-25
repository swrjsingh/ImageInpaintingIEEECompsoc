import os
import shutil
from flask import Flask
from flaskApp.routes import main_blueprint

def App():

    #delete prev images
    if(os.path.exists('flaskApp\images')):
        shutil.rmtree('flaskApp\images')

    if(os.path.exists('flaskApp\masks')):
        shutil.rmtree('flaskApp\masks')
        
    if(os.path.exists('flaskApp\inpainted')):
        shutil.rmtree('flaskApp\inpainted')
    
    #create new folders
    os.mkdir('flaskApp\images')
    os.mkdir('flaskApp\inpainted')
    os.mkdir('flaskApp\masks')

    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    return app