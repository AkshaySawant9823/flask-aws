from flask import Flask

application = Flask(__name__)

@application.route("/")
def homepage():
    return "Hello, Akshay..!!!"

# if __name__=="__main__":
#     application.run(debug=True)