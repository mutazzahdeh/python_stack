from flask import Flask, render_template, request, redirect , session

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/' , methods = ['POST'])
def index():
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    lang = request.form['lang']
    comment = request.form['text']
    return render_template("index2.html", name = name , location = location , lang = lang , comment = comment)

if __name__ == "__main__":
    app.run(debug=True)
