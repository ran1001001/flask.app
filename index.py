from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/view")
def view():
    contacts = [
            {
                    "first": "John",
                    "last": "Smith",
                    "email": "john@example.com"
                },
            {
                    "first": "Dora",
                    "last": "Crandith",
                    "email": "dcran@example.com"
                },
            {
                    "first": "Dana",
                    "last": "White",
                    "email": "dwhite@example.com"
                },
            {
                    "first": "Dana",
                    "last": "Black",
                    "email": "dblack@example.com"
                },
            {
                    "first": "Dana",
                    "last": "Brown",
                    "email": "dbrown@example.com"
                },
            {
                    "first": "Joe",
                    "last": "Rogan",
                    "email": "jrogan@example.com"
                }
        ]

    search = request.args.get("q")

    # contacts_set needs to List/s of dicts
    if search is not None:
        for index, first_name in enumerate(contacts):
            if first_name["email"].lower() == search:
                contacts_set = [contacts[index]]
                break
            else:
                contacts_set = None
    else:
        contacts_set = contacts
    if contacts_set is None:
        return "No contact of email \"{}\" exist.".format(search)
    return render_template("index.html", contacts=contacts_set)


@app.route("/")
def index():
    return redirect("/view")
