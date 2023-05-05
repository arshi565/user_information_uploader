from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file)
    name = data['Name'].values[0]
    email = data['Email'].values[0]
    phone = data['Phone'].values[0]
    return render_template('form.html', name=name, email=email, phone=phone)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    # Save the user's information to a database
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
