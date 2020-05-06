from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/likes")
def like():
	return render_template("likes.html")

@app.route("/skills")
def skill():
	return render_template("skills.html")

@app.route("/possessions")
def possess():
	return render_template("possessions.html")