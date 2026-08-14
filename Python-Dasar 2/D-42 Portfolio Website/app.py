
# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request, redirect, url_for, flash
# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='Portfolio_app/templates', static_folder='Portfolio_app/static')
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Project Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)

# Initialize Database
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('All fields are required', 'error')
        else:
            flash('Message sent successfully', 'success')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    
