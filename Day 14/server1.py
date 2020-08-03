from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_logSave


app = Flask(__name__)

# http://localhost:8000
@app.route('/', methods = ['GET'])
def hello_world():
    #can write any code
    return 'Hello world. This is Flask' 


@app.route('/abc', methods = ['GET'])
def abc_view():
    #can write any code
    return 'Hello world. This is abc wonderland' 


@app.route('/scraper', methods = ['POST'])
def box_office_scrapper_view():
    trigger_logSave()
    scrape_runner()
    return {'data':[1,2,3,5]}  