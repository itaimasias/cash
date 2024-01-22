from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your actual code
correct_code = "hi123"


@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    code_valid = False

    if request.method == 'POST':
        entered_code = request.form.get('code')

        if entered_code == correct_code:
            code_valid = True
        else:
            error = 'Invalid code. Please try again.'

    return render_template('home.html', error=error, code_valid=code_valid)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
