# Matthew Lane (ml2162) - CSE 4283-01: Assignment 2

# Import all the functions from the bmi file
from bmi import *
# Import the flask app from the main file
from main import app

# Here we will test if the main page loads correctly.


def test_home_page():
    # Utilize Flask's built-in test client
    # for simulating browser requests.
    client = app.test_client()

    # Visit the homepage
    response = client.get('/')

    # Check if the title appears in the response
    assert "<title>BMI Calculator</title>".encode("UTF-8") in response.data
    assert response.status_code == 200


def test_perform_bmi_calculation():
    # Utilize Flask's built-in test client
    # for simulating browser requests.
    client = app.test_client()

    # Test with known working data
    test_data = {
        "feet": "5",
        "inch": "3",
        "pounds": "120"
    }
    response = client.post('/', data=test_data)
    assert """<td id="results">120<span id="unit">lbs</span></td>""".encode(
        "UTF-8") in response.data
    assert """<td id="results">5<span id="unit">'</span></td>""".encode(
        "UTF-8") in response.data
    assert """<td id="results">3<span id="unit">"</span></td>""".encode(
        "UTF-8") in response.data
    assert """<td id="results" colspan="2">21.8</td>""".encode(
        "UTF-8") in response.data
    assert """<td id="results" colspan="2">Normal weight</td>""".encode(
        "UTF-8") in response.data
    assert response.status_code == 200

    # Test with data missing
    response = client.post('/')
    assert response.status_code == 400

    # Test with feet missing
    test_data = {
        "feet": "",
        "inch": "3",
        "pounds": "120"
    }
    response = client.post('/', data=test_data)
    assert """<p id="error">Please enter a valid number in feet above or equal to 0.</p>""".encode(
        "UTF-8") in response.data
    assert response.status_code == 200

    # Test with inches missing
    test_data = {
        "feet": "5",
        "inch": "",
        "pounds": "120"
    }
    response = client.post('/', data=test_data)
    assert """<p id="error">Please enter a valid number in inches above or equal to 0.</p>""".encode(
        "UTF-8") in response.data
    assert response.status_code == 200

    # Test with pounds missing
    test_data = {
        "feet": "5",
        "inch": "3",
        "pounds": ""
    }
    response = client.post('/', data=test_data)
    assert """<p id="error">Please enter a valid number in pounds above or equal to 1.</p>""".encode(
        "UTF-8") in response.data
    assert response.status_code == 200

# Here we will test if the verify_measurement function
# works as expected.


def test_verify_measurement():
    # Test a scenario that should work
    assert verify_measurement("0", "test", 0) == (0, None)
    # Test str check
    assert verify_measurement(1.5, "test", 0) == (
        1.5, "Please enter a valid number in test above or equal to 0.")
    # Test int check
    assert verify_measurement("not int", "test", 0) == (
        "not int", "Please enter a valid number in test above or equal to 0.")
    assert verify_measurement("1.5", "test", 0) == (
        "1.5", "Please enter a valid number in test above or equal to 0.")
    # Test floor check
    assert verify_measurement("0", "test", 1) == (
        0, "Please enter a valid number in test above or equal to 1.")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Underweight.


def test_calculate_bmi_underweight():
    # For the given range (-infinity, 18.5), we calculate the
    # following Weak N x 1 points...
    # OFF = 18.4
    assert calculate_bmi(63, 101.43) == (18.4, "Underweight")
    # ON = 18.5
    assert calculate_bmi(63, 101.98) == (18.5, "Normal weight")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Normal weight.


def test_calculate_bmi_normal_weight():
    # For the given range [18.5, 25), we calculate the
    # following Weak N x 1 points...
    # OFF = 18.4
    assert calculate_bmi(63, 101.43) == (18.4, "Underweight")
    # ON = 18.5
    assert calculate_bmi(63, 101.98) == (18.5, "Normal weight")
    # INT = 21.8
    assert calculate_bmi(63, 120.17) == (21.8, "Normal weight")
    # OFF = 24.9
    assert calculate_bmi(63, 137.26) == (24.9, "Normal weight")
    # ON = 25
    assert calculate_bmi(63, 137.81) == (25, "Overweight")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Overweight.


def test_calculate_bmi_overweight():
    # For the given range [25, 30), we calculate the
    # following Weak N x 1 points...
    # OFF = 24.9
    assert calculate_bmi(63, 137.26) == (24.9, "Normal weight")
    # ON = 25
    assert calculate_bmi(63, 137.81) == (25, "Overweight")
    # INT = 27.5
    assert calculate_bmi(63, 151.59) == (27.5, "Overweight")
    # OFF = 29.9
    assert calculate_bmi(63, 164.82) == (29.9, "Overweight")
    # ON = 30
    assert calculate_bmi(63, 165.38) == (30, "Obese")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Obese.


def test_calculate_bmi_obses():
    # For the given range [30, infinity), we calculate the
    # following Weak N x 1 points...
    # OFF = 29.9
    assert calculate_bmi(63, 164.82) == (29.9, "Overweight")
    # ON = 30
    assert calculate_bmi(63, 165.38) == (30, "Obese")
