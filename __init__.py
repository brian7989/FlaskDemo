from flask import Flask, g, make_response, Response, render_template, url_for, redirect

app = Flask(__name__)
app.url_map.host_matching = True
app.debug = True


@app.before_request
def before_request():
    print("before_request!!!")
    g.str = "한글"


@app.route('/')
def run_this():
    return make_response(render_template('index.html'), 200, {'name': 'brian', 'gender': 'male'})


@app.route('/test_wsgi', host="abc.com")
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Length', str(len(body))),
                   ('Name', 'Brian')]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)


if __name__ == '__main__':
    app.run()
