# Python Chess Tournament Program

This repository contains the work that has been done so far on the chess tournament program.
In addition, it has the completed Chess Tournament program.

### Models

This package contains the models already defined by the application:
* `Player` is a class that represents a chess player
* `Club` is a class that represents a chess club (including `Player`s)
* `ClubManager` is a manager class that allows to manage all clubs (and create new ones)
* `Tournament` is a class that represents a tournament (including `Round`s and `Match`es)
* `TournamentManager` is a manger class that allows to manage all tournaments (and create new ones)

### Main application

The main club application is controlled by `manage_clubs.py`.
The main tournament appliation is controlled by `manage_tournament.py`.

### How to use the application:

To run the chess tournament program:
1. Install all the dependencies stored in `requirements.txt`, this can be done by using `pip install-r requirements.txt`.
2. To run the script, run from the directory the file is installed is `python manage_tournament.py`.

To run the chess club program:
1. Install all the dependencies stored in `requirements.txt`, this can be done by using `pip install-r requirements.txt`.
2. To run the script, run from the directory the file is installed is `python manage_clubs.py`.

### flake8 html generation
To generate a html flake8 report and store it in the directory, `flake8_report`, the following steps must be undertaken.
(Note: Step 1 can be skipped if you have done it above.)

1. Install all the dependencies stored in `requirements.txt`, this can be done by using `pip install-r requirements.txt`.
2. To generate the html flake8 report, run from the project directory: `flake8 --format=html --htmldir=flake8_report`
