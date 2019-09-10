from flask import Flask, render_template, request, make_response, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("/home.html")

@app.route('/resume')
def hello_world():
    return render_template("/resume.html")

@app.route('/projects')
def hello_world():
    return render_template("/projects.html")

@app.route('/blogs')
def hello_world():
    return render_template("/blogs.html")

@app.route('/about-me')
def hello_world():
    return render_template("/about-me.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')
