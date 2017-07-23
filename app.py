from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
db = dataset.connect("postgres://wyatfdlebnriti:2b530a18fd94064e074dc26661c0c5e9d7c0284f5789a6a9a38d2fca15a62892@ec2-54-83-49-44.compute-1.amazonaws.com:5432/d9skv55jqn2qvb")


@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /list
@app.route('/list')
def list():
	return render_template('list.html')

# TODO: route to /feed
@app.route('/feed')
def feed():
	return render_template('/feed.html')


# TODO: route to /register
@app.route('/')
@app.route('/register')
def register():
	return render_template('register.html')
# TODO: route to /error
@app.route('/error')
def error():
	return render_template("register.html")

if __name__ == "__main__":
    app.run(port=3000)











