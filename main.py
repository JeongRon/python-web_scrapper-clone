from flask import Flask

app = Flask("JobScrapper")


@app.route("/")
def home():
    return "<h1>hey there</h1><a href='/hello'>go to hello</a>!"


@app.route("/hello")
def hello():
    return "hello you!"


app.run("127.0.0.1")
