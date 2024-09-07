from flask import Blueprint, render_template


profile_route = Blueprint("profile", __name__, url_prefix="/user", static_folder='static', template_folder='templates')

@profile_route.route("/") # users/
def user_page():
    return render_template("user_index.html")

@profile_route.route("/students") # users/students
def students_page():
    return render_template("students.html")

