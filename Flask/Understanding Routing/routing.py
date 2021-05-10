from flask import Flask  
app = Flask(__name__) 


@app.route("/")
def hello_world():
    return "Hello World!    "


@app.route("/dojo")
def dojo():
    return "dojo"


@app.route("/say/<name>")
def say(name):
    return f"Hello {name}!"


@app.route("/repeat/<int:num>/<name>")
def hello(num,name):
    str1=""
    for i in range (num):
        str1+=f"{name}" + "\n"
    return str1


@app.route("/<str>")
def sorry(str):
    return "Sorry! No response. Try again"

   
if __name__=="__main__":    
    app.run(debug=True) 