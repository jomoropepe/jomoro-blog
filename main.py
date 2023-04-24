from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/f84b7fbd75cb98e157ab")
data = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<id>')
def post(id):
    requested_blog = None
    for posts in data:
        print(posts)
        print(posts["id"])
        if str(posts["id"]) == id:
            requested_blog = posts
    return render_template("post.html", post_data=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)