from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('homologacao'))

@app.route('/homologacao-assinatura')
def homologacao():
    return render_template('homologacao.html')

if __name__ == '__main__':
    app.run(debug=True)
