from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
db = dataset.connect("postgres://wyatfdlebnriti:2b530a18fd94064e074dc26661c0c5e9d7c0284f5789a6a9a38d2fca15a62892@ec2-54-83-49-44.compute-1.amazonaws.com:5432/d9skv55jqn2qvb")


@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /list


# TODO: route to /feed
@app.route('/feed')
def feed():
	return render_template('/feed.html')
@app.route('/contactus')

def contactus():
	return render_template('/contactus')


# TODO: route to /register
@app.route('/')
@app.route('/register')
def register():
	return render_template('register.html')


# TODO: route to /error
# @app.route('/error')
# def error():
# 	return render_template("register.html")
@app.route ('/showall')
def showall():
	users = db ["users"]
	allusers = list(users.all())
	return render_template ("showall1.html", users= allusers)

@app.route('/users' ,methods=["POST"])
def users():
	# if username is in the db
		# print an error saying username is already taken
	# otherwise
		# register the user
		# sucessful login



	
	form = request.form
	firstname= form["first name"]
	lastname= form["last name"]
	email = form["email"]
	username= form["username"]
	link = form["link"]
	contactsTable = db["users"]
	hometown = form["hometown"]
	entry = {"firstname":firstname ,"lastname":lastname ,"username":username, "email":email , "link":link, "hometown":hometown }
	nameTocheck = username
	result = list(contactsTable.find(username=nameTocheck))
	print len(result)
	if len(result) == 0:
		taken = 0
		contactsTable.insert(entry)	
		return redirect("/showall")
	else :
		taken = 1
		return render_template("register.html", taken = taken)
		print list(contactsTable.all())	

if __name__ == "__main__":
    app.run(port=3000)











