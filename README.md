Python Selenium Automation Test Script

This is a Python script that uses Selenium to automate the login and checkout process on the Sauce Demo website.
Requirements

    Python 3.x
    Selenium

To install the required packages, run:

```bash
pip install -r requirements.txt
```

Usage

To run the script, specify the browser you want to use with the --browser flag. The supported browsers are 'chrome', '
firefox', 'edge', 'safari', or 'opera'.

```bash
pytest --browser firefox
```

Description

    The script automates the login and checkout process on the Sauce Demo website.
    It logs in with predefined credentials.
    Adds a randomly selected item to the cart.
    Proceeds to checkout.
    Completes the order and confirms the success.

Logging

The script uses Python's built-in logging module to log the process. Errors and important information will be logged to
the console during execution.
Note

Note

Ensure that the appropriate web driver for your chosen browser is installed and available in your system's PATH.