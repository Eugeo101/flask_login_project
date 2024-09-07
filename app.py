from flask import Flask, render_template, url_for, redirect
from users.profile import profile_route

app = Flask(__name__)
app.register_blueprint(profile_route)




if __name__ == "__main__":
    app.run(debug=True, port=5000)