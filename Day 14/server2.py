
from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_logSave

app = FastAPI()

@app.get("/")
def hello_world():
    return {"hello": "world"}

@app.get("/abc")
def abc_view():
    return {"data": [1,2,3]}


@app.post("/scraper")
def scrape_runner_view():
    trigger_logSave()
    scrape_runner()
    return {"data": [1,2,3]}