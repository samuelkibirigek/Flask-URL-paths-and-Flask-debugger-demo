from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "This is the home page!"


# a single variabe
@app.route("/greet/<name>")
def greeting(name):
    return f"{name}, this method takes a variable returned by decorator and greets you.Hello {name}!"

# Specifying variable type aside from the default string using converter


# taking a path variable ie one with a forward slash
@app.route("/dishes/<path:food>")
def fav_food(food):
    return f"My favorite dish is {food}"


# working with integers
@app.route("/age/<name>/<int:age>")
def age(name, age):
    return f"Hello {name}, you said you are {age + 2} years old!"


# Setting the debug mode to true helps reset the server on saving file and also in debugging
if __name__ == "__main__":
    app.run(debug=True)

