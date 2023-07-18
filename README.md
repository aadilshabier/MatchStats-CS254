### MATCHSTATS

MatchStats is a football tournament management app developed using Django framework. Designed to keep track of all the teams, matches, players and all other aspects of the football tournament. Incorporated in it is a role based management system allowing the administrators and managers to access different levels of information and edit permissions.

## INSTALLATION

FOR LOCAL USE-
1.  Clone the repository `git clone`
2.  Navigate to the project directory
3.  Create a virtual environment
4.  Install the project dependancies `pip install -r requirements.txt`
5.  Set up the database:
        1. Update the database settings in settings.py according to your environment.
        2. Run migrations: 
        `python manage.py migrate`
6.  Start the development server: python manage.py runserver
7.  Access the app in your web browser at http://localhost:8000

## FEATURES

Role-based management system with different access levels for administrators, managers, and players.
User authentication and account management.
Team management: create, update, and delete teams.
Player management: add, edit, and remove player details.
Match management: schedule matches, record match results, and view match statistics.

## Usage
Using the admin credential given below local changes can be made to the apps managers
# Admin
    - Username: admin
    - Password: admin

Managers added can use their credentials to login.
Based on the role that the app user is they have different permissisons for the updation and vewing of data.