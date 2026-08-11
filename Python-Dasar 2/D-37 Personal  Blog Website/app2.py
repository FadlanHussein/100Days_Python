from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Welcome to My Blog')

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/contact')
def contact():
    return "This is the Contact page."

if __name__ == '__main__':
    app.run(debug=True, port=5002)