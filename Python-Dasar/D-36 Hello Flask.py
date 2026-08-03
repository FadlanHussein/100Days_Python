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
# %% Kasus 1:
from flask import Flask

# Create Flask App
app = Flask(__name__)

# Define a route
@app.route('/')
def hello():
    return "Hello, Flask!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True) 
# %% Flask Templates
from flask import render_template

# Create Flask App
app = Flask(__name__)

# Define a route
@app.route('/')
def hello():
    return render_template('D-36 template.html', name='Flask')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
