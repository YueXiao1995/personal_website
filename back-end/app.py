from flask import Flask, render_template, request, make_response, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/home')
def hello_world():
    return render_template("/home.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')
