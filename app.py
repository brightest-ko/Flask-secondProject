from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return "hi! flask!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        c()
    else:
        show_the_login_form()


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run(debug = True)
