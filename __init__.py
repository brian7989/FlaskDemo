from flask import Flask, g, make_response, Response, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def run_this():
    return "Hi"


if __name__ == '__main__':
    app.run()
