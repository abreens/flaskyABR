from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
        return '<h1>Welcome Welcome Welcome</h1>'


@app.route('/user/<name>')
def user(name):
        return '<h1>Hello, {}!<h1>'.format(name)


@app.route('/about')
def about_me():
        return '<h1>About About About</h1>'


@app.route('/portfolio')
def portfolio():
        return '<h1>Portfolio Portfolio Portfolio</h1>'


if __name__ == '__main__':
        app.run()
