# Blog
Credentials for the demo user:
Username: admin
Password: admin

This project was built using 3 core technologies:
1. Flask for the backend 
2. Flask-SQLAlchemy for handling of the data base
3. Flask-login to help managing the users


The structure of the files is as follows:
Instance: Folder that contains the sqlite database.
Posts: Module that handles everything post related
Users: Module that handles everithing user related
App: File that contains and runs the Flask Application
Db: File that contains and builds the Database
Settings: File that contains constant variables

The application is divided in 2 modules, the user module and the posts module
Each module contains a models.py file that contains the python representation
of a db table in a class format. And a views.py that contains the endpoints
that will execute the logic of each specific module.
The users views.py contains:
- Login endpoint: Gets credentials, checks the validity of them and logs the user in
- Logout endpoint: Logs out the user

The posts module views.py contains:
- Home endpoint: Displays a list of posts starting with the newest
- Create post endpoint: Gets the data from a form, validates the data and
creates a row in the posts table with the form data.
- Edit post endpoint: Gets an id from the url and displays a form with the information of
the post with the corresponding id. If a post request is made to this endpoint
the data of the post will be updated.
- Delete post endpoint: Gets an id from the url and deletes the post corresponding to
that id.


