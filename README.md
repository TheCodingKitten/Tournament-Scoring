# Tournament Scoring

Created by Henry Nevill

https://github.com/TheCodingKitten/Tournament-Scoring/


## Requirements

Python 3 (Tested on Python 3.13.1)
	Python csv module

## Usage

No install is necessary, just run `TournamentScoring.py` in a terminal emulator (Windows Powershell / Linux terminal)

Import or create teams


## Subcommands within program

| Command     | Function                        |
|-------------|---------------------------------|
| help        | Displays a help message         |
| exit        | Exits program                   |
| addteam     | Begins the team adding function |
| removeteam  | Removes a team                  |
| teams       | Display all teams               |
| events      | Shows all events                |


### Adding team

After entering the `addteam` command, you will be prompted to add a team name.
You will then be prompted to enter the names of each member, seperated by a newline.
To stop entering new names, leave the value blank followed by a newline.
If the team was added successfully, a message will be shown with the team number.


### Listing current teams

When current teams are listed, either using the `teams` command or at the beginning of the removeteam function,
the teams will be listed with the following values:
Number: Name: Members

E.g.

1: Smarties: Bob

2: Cheese: James, Charlie

