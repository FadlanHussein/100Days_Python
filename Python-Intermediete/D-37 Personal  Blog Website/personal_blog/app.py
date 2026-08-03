from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='Static')

# Sample Blog Posts
posts = [
    {'id': 1, 'title': "Introduction to Flask", 'content': "This is the content of the first post.", 'author': "John Doe", 'date_posted': "2024-06-01"},
    {'id': 2, 'title': "Advanced Flask Techniques", 'content': "This is the content of the second post.", 'author': "Jane Smith", 'date_posted': "2024-06-02"}
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5004)