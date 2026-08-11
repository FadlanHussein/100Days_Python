from flask import Flask

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Alias route for home page
@app.route('/home')
def home_alias():
    return "Welcome to the Home Page!"

# Dynamic Route
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Showing post with ID: {post_id}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)