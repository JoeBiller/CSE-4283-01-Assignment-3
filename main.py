# Matthew Lane (ml2162) - CSE 4283-01: Assignment 3
# Import only the necessary parts of Flask
from flask import Flask, render_template, request
# Import the code from the previous assignment (slightly modified)
import bmi

# Create our Flask app
app = Flask(__name__)

# This function will display the BMI calculation form
# to users who visit the root path.


@app.get("/")
def show_bmi_form():
    return render_template("bmi_form.html")

# This function will verify the user has provided all the
# required measurements, perform a BMI calculation on those
# measurements, then display it to the user.


@app.post("/")
def perform_bmi_calculation():
    # Verify feet were provided correctly
    feet, error = bmi.verify_measurement(request.form["feet"], "feet", 0)
    if error:
        return render_template("bmi_form.html", error_message=error)

    # Verify inches were provided correctly
    inch, error = bmi.verify_measurement(request.form["inch"], "inches", 0)
    if error:
        return render_template("bmi_form.html", error_message=error)

    # Verify pounds were provided correctly
    pounds, error = bmi.verify_measurement(request.form["pounds"], "pounds", 1)
    if error:
        return render_template("bmi_form.html", error_message=error)

    # Combine feet and inches
    inches = (feet * 12) + inch

    # Perform the calculation
    bmi_value, bmi_category = bmi.calculate_bmi(inches, pounds)

    success = {
        "feet": feet,
        "inches": inch,
        "pounds": pounds,
        "bmi_value": bmi_value,
        "bmi_category": bmi_category
    }

    # Display results to user
    return render_template("bmi_form.html", success=success)
