from flask import Flask, redirect, url_for, render_template

app = Flask (__name__)

@app.route ("/")
def home ():
     return render_template("index.html", content = "Hello! this is the main page <h1>HELLO<h1>", r=2)

@app.route ("/<name>")
def yoyo (name):
     return render_template("index.html", content = name, r=2, )


if __name__ == "__main__":
    app.run()
    
