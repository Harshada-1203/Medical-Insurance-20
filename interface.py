#api.py
#interface.py
#run.py
# create env
  #1. python -m venv env_name
  #2. cmd
  #3. copy relative path of activate.bat
# pip install Flask
# pip install pandas
# pip install scikit-learn
# to install postman : go to extension (CTRL +SHIFT + X)
# https://www.postman.com/downloads/

from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

user_creds = {"username" : "admin",
              "password" : "admin@2024"}

@app.route("/")
def login_page(): # home api
    return "We are at home api"


@app.route("/test_login",methods = ["POST","GET"])
def test_login():
    if request.method == "POST":
        data_dict = request.form
        username = data_dict["username"]
        password = data_dict["password"]
        print("username is",username)
        print("password is",password)

        if username == user_creds["username"] and password == user_creds["password"]:
            return jsonify({"status": "Successful","message": "Login Successful"})
        else:
            return jsonify({"status": "UnSuccessful","message": "Invalid Credentials"})

if __name__ == "__main__":
    app.run()
