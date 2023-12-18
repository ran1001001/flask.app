from flask import Flask, redirect, render_template, request

app = Flask(__name__)

contacts = {
        "first_names": ["John", "Dora", "Dana", "Dana", "Dana", "Joe"],
        "last_names": ["Smith", "Crandith",
                       "White", "Black", "Brown", "Rogan"
                       ],
        "emails": ["john@example.com", "dcran@example.com",
                   "dwhite@example.com", "dblack@example.com",
                   "dbrown@example.com", "jrogan@example.com"]
    }


@app.route("/contacts")
def view():
    search = request.args.get("q")

    # contacts_set is set to to dictionary of "key:<List>"
    if search is not None:
        if search in contacts["emails"]:
            # index of a contact
            index = contacts["emails"].index(search)
            contacts_set = {"first_names": [contacts["first_names"][index]],
                            "last_names": [contacts["last_names"][index]],
                            "emails": [contacts["emails"][index]]}
        else:
            message = "No contact of email \"{}\" exist.".format(search)
            return render_template("redirect.html", message=message)
    else:
        contacts_set = contacts
    return render_template("index.html", contacts=contacts_set)


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/add_contact")
def add():
    return render_template("add.html")
