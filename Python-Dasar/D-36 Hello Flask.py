# Welcome to day 36 of your 100 Days of Python Challenge.
# Today we will transition from desktop GUI development with Tkinter to web development with flask.
# Flask is a lightweight and flexible web framework for building web applications in Python.
# By the end of the day, you will build your first Hello Flask app, where users can interact with a
# simple web page served by your Python backend.
#
# So let's look at what you learned today.
# First, what is flask?
# Next we're going to look at setting up flask.
# Next we're going to go into creating your first flask route.
# Next we're going to look at understanding flask templates.
# And finally our day 36 project which is a Hello flask app.
#
# So let's look at what is flask.
# Now flask is a micro web framework for Python.
# It's designed to be simple, lightweight, and highly customizable.
# flask is often used for building APIs, dynamic websites, and microservices.
#
# Now why use flask?
# It's because it's lightweight, which is minimal boilerplate code, and that's what we will look at.
# It's scalable, easily expandable for larger projects.
# It's flexible.
# It supports extension for advanced features and is pythonic, which means it's easy integration with
# Python libraries.
#
# Let's talk about setting up flask.
# First, let's go ahead with the installation.
# Ensure flask is installed on your system.
# You can run: pip install flask
# To verify installation use: python -m flask --version

from flask import Flask, render_template

# %% Kasus 1: Membuat instance Flask
app = Flask(__name__)

# %% Kasus 2: Route dasar untuk halaman home
@app.route("/")
def home():
    return render_template("index.html")

# %% Kasus 3: Route dinamis dengan parameter URL
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)

# %% Kasus 4: Bonus route About
@app.route("/about")
def about():
    return render_template("about.html")

# %% Kasus 5: Custom 404 page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# %% Kasus 6: Menjalankan aplikasi Flask
if __name__ == "__main__":
    app.run(debug=True)
