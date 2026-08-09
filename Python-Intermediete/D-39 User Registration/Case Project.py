# pyrefly: ignore [missing-import]
from flask import Flask, flash, redirect, render_template_string, request, url_for
# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy
# pyrefly: ignore [missing-import]
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///users.db"
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

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not email or not password:
            flash('Harap isi semua data', 'error')
            return 'Harap isi semua data', 400

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return 'Username atau email sudah terdaftar', 400

        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)

        try:
            db.session.add(user)
            db.session.commit()
            flash('Pendaftaran berhasil!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Terjadi kesalahan saat mendaftar', 'error')
            return 'Terjadi kesalahan saat mendaftar', 500

    return render_template_string('''
        <h1>Registration Form</h1>
        <form method="post" action="{{ url_for('register') }}">
            <p>Username: <input type="text" name="username" required></p>
            <p>Email: <input type="email" name="email" required></p>
            <p>Password: <input type="password" name="password" required></p>
            <button type="submit">Register</button>
        </form>
    ''')

# Home Route
@app.route("/")
def index():
    return render_template_string('''
        <h1>Welcome to My App</h1>
        <p>Ini adalah halaman utama yang terpisah.</p>
        <ul>
            <li><a href="{{ url_for('register') }}">Go to Register</a></li>
            <li><a href="{{ url_for('login') }}">Go to Login</a></li>
        </ul>
    ''')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    return "Login functionality is not implemented yet."

if __name__ == '__main__':
    app.run(debug=True, port=5006)