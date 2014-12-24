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

if __name__ == '__main__':
    app.run(debug=True)
