from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando um banco de dados simples
users = {'carlos': '123456', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Autenticação bem-sucedida
        return redirect(url_for('profile.html', username=username))
    else:
        # Autenticação falhou
        return render_template('index.html', error='Login falhou. Verifique suas credenciais.')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
