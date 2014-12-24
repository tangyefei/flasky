from flask import Flask, render_template

app = Flask(__name__)

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





if __name__ == '__main__':
    app.run(debug=True)
