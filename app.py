from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('simpleApp.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        college_level = request.form['college_level']
        classes_taken = request.form['classes_taken']
        class_expectation = request.form['class_expectation']

        with open('data.txt', 'a') as f:
            f.write(f"{name},{email},{college_level},{classes_taken},{class_expectation}\n")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
