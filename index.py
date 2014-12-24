from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

class Human():
    def somemethod(self):
        return 'what the fucking world!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    mydict = {"key": "To Be or Not To Be"}
    mylist = ['it', 'is', 'a', 'problem']
    myintvar = 0
    myobj = Human()

    return render_template('user.html', name=name, mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)

@app.route('/flow')
def flow():
    user = 'tangyefei'

    return render_template('flow.html', user=user)

@app.route('/loop')
def loop():
    comments = ["To Be", "Or", "Not To Be"]

    return render_template('loop.html', comments=comments)


@app.route('/macro')
def macro():
    comments = ["To Be", "Or", "Not To Be"]

    return render_template('macro.html', comments=comments)


@app.route('/comments')
def comments():
    comments = ["To Be", "Or", "Not To Be"]

    return render_template('comments.html', comments=comments)

@app.route('/extends')
def extends():
    return render_template('child.html')

@app.route('/bootstrap/<name>')
def bootstrap(name):
    return render_template('bootstrap.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
