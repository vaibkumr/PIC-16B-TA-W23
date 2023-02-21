from flask import Flask, render_template, request, redirect, url_for
import sqlutils


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    assert request.method == 'POST', "Weird... this shouldn't happen. EVER."
    username = request.form['username']
    message = request.form['message']
    sqlutils.save_message(username, message)
    return redirect(url_for('messages', username=username))

@app.route('/messages/<username>')
def messages(username):
    messages = sqlutils.fetch_messages(username)
    return render_template('messages.html', username=username, messages=messages)

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/hello/<name>/')
def hello_name(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    sqlutils.create_table()
    # app.run(port=8888)
    app.run(host='0.0.0.0', port=3000)

