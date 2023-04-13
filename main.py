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
    # Set the form to default values
    last = {
        "feet": 5,
        "inch": 9,
        "pounds": 140
    }

    return render_template("bmi_form.html", last=last)

# This function will verify the user has provided all the
# required measurements, perform a BMI calculation on those
# measurements, then display it to the user.


@app.post("/")
def perform_bmi_calculation():
    def return_error(error):
        # Set the form to user's previous input
        last = {
            "feet": request.form["feet"],
            "inch": request.form["inch"],
            "pounds": request.form["pounds"]
        }
        # Return the error message
        return render_template("bmi_form.html", error_message=error, last=last)

    # Verify feet were provided correctly
    feet, error = bmi.verify_measurement(request.form["feet"], "feet", 0)
    if error:
        return return_error(error)

    # Verify inches were provided correctly
    inch, error = bmi.verify_measurement(request.form["inch"], "inches", 0)
    if error:
        return return_error(error)

    # Verify pounds were provided correctly
    pounds, error = bmi.verify_measurement(request.form["pounds"], "pounds", 1)
    if error:
        return return_error(error)

    # Combine feet and inches
    inches = (feet * 12) + inch

    # Perform the calculation
    bmi_value, bmi_category = bmi.calculate_bmi(inches, pounds)

    # Build success table dictionary
    success = {
        "feet": feet,
        "inches": inch,
        "pounds": pounds,
        "bmi_value": bmi_value,
        "bmi_category": bmi_category
    }

    # Set the form to user's previous input
    last = {
        "feet": feet,
        "inch": inch,
        "pounds": pounds
    }

    # Display results to user
    return render_template("bmi_form.html", success=success, last=last)
