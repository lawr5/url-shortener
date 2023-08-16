# URL Shortener

This URL Shortener is a web app that allows users to take URLs with the http or https scheme and associate them to a short URL.

## Tools Used

- Flask
- SQLAlchemy
- Jinja2

## Setup/Run

First, clone this repository. After cloning the repository you will need to create and activate a virtual environment. Next, install the packages in the requirements.txt file into your virtual environment. To run the app type flask --app src.app run on the command line and type localhost:5000 in the browser or type flask --app src.app run --host=<your_computer_hostname> on the command line and type <your_computer_hostname>:5000 in the browser. This should start the app and create the table(s) in a SQLite database from the model(s) that have been defined.
