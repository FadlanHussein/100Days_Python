from flask import Flask, render_template, request, redirect, url_for, flash
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

# Initialize Database and Seed Sample Data if Empty
with app.app_context():
    db.create_all()
    if Project.query.count() == 0:
        sample_projects = [
            Project(
                title="Mini Weather API",
                description="RESTful API sederhana menggunakan Flask untuk menyajikan data cuaca.",
                image_url="https://images.unsplash.com/photo-1592210454359-9043f067919b?w=500",
                link="#"
            ),
            Project(
                title="User Registration System",
                description="Sistem registrasi & autentikasi user menggunakan Flask-SQLAlchemy dan Password Hashing.",
                image_url="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500",
                link="#"
            ),
            Project(
                title="Personal Blog Website",
                description="Platform blog pribadi interaktif berbasis Flask dengan templating Jinja2.",
                image_url="https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=500",
                link="#"
            )
        ]
        db.session.bulk_save_objects(sample_projects)
        db.session.commit()

# Home Route
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Project Detail Route
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', project=project)

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('Harap isi semua kolom pendaftaran.', 'error')
        else:
            flash('Pesan Anda berhasil terkirim! Terima kasih telah menghubungi.', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
