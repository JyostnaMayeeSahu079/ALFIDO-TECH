from flask import Flask, render_template, request, redirect

app = Flask(__name__)

FILE_NAME = "feedback.txt"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']

    with open(FILE_NAME, 'a') as file:
        file.write(f"{name}: {feedback}\n")

    return redirect('/view')

@app.route('/view')
def view():
    try:
        with open(FILE_NAME, 'r') as file:
            feedbacks = file.readlines()
    except:
        feedbacks = []

    return render_template('view.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)