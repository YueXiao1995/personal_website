from flask import Flask, render_template, request, make_response, redirect, url_for, send_from_directory

app = Flask(__name__)

is_under_maintenance = False

@app.route('/')
def home():
    return render_template("/maintenance.html")
    #return render_template("/home.html")

@app.route('/resume')
def resume():
    return render_template("/resume.html")

@app.route('/projects')
def projects():
    return render_template("/projects.html")

@app.route('/blogs')
def blogs():
    return render_template("/blogs.html")

@app.route('/about-me')
def about_me():
    return render_template("/about-me.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')
