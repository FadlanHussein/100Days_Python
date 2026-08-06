import os

from flask import Flask, redirect, render_template_string, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.instance_path = os.path.join(os.getcwd(), 'instance')
os.makedirs(app.instance_path, exist_ok=True)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'users.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


# Create Database tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template_string('''
        <h1>Registration Form</h1>
        <form method="post" action="{{ url_for('register') }}">
            <p>Username: <input type="text" name="username" required></p>
            <p>Email: <input type="email" name="email" required></p>
            <p>Password: <input type="password" name="password" required></p>
            <button type="submit">Register</button>
        </form>
    ''')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not email or not password:
            return 'Harap isi semua data', 400

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return 'Username atau email sudah terdaftar', 400

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success', username=username))

    return redirect(url_for('index'))


@app.route('/success/<username>')
def success(username):
    return f'Registrasi berhasil untuk {username}'


if __name__ == '__main__':
    app.run(debug=True, port=5005)