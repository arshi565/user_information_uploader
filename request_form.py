from flask import Flask, render_template, request

app = Flask(__name__)

def validate_data(name, email, phone):
    errors = []
    if not name:
        errors.append('Please enter your name.')
    if not email:
        errors.append('Please enter your email.')
    if not phone:
        errors.append('Please enter your phone number.')
    return errors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        errors = validate_data(name, email, phone)
        if not errors:
            # Save the user's data to a file or database
            return render_template('form.html', success=True)
        else:
            return render_template('form.html', errors=errors)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
