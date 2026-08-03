from flask import Flask, render_template

# %% Kasus 1: route sederhana
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

# %% Kasus 2: render template dan route dinamis
@app.route('/template')
def show_template():
    return render_template('index.html', name='Flask')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
