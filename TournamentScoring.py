#!/usr/bin/env python3

# Tournament Scoring and Management
# Created by Henry Nevill
# https://github.com/TheCodingKitten/

# Define available commands and meanings
mainCommands = {
"help": "Displays this help message",
"exit": "Exit program",
"addteam": "Begins the team adding function",
"removeteam": "Removes a team",
"teams": "Display all teams",
"events": "Shows all events",
}

def commandHelp(oneCommand = None):
	print("Showing command help. Format = `command: meaning`")
	for command, meaning in mainCommands.items():
		print(f"{command}: {meaning}")

# Define team event names and types
teamEvents = {
"Five a side Football": "sport",
"Golf": "sport",
"Tug of war": "sport",
"Chess": "academic",
"General knowledge quiz": "academic",
}

# Define individual event names and types
individualEvents = {
"Darts": "sport",
"Tennis": "sport",
"Golf": "sport",
"Chess": "academic",
"General knowledge quiz": "academic",
}

# Initialise participants list. Entries will be stored as a list within this list to allow for teams and individuals
# Format for team list: Team ID, Team Name, Score, Member Names...
teams = [[1, 'Munchkins', 0, 'Tom', 'Charlie'], [2, 'Smarties', 0, 'Harry', 'Patricia']]

totalTeams = 0

# Function to add team and members
def addTeam(teamID):
	print("Adding team. Enter a blank value to stop adding members.")
	team = [teamID]
	team.append(input("Team name: "))
	team.append(0)
	print("Add team member names: ")
	while True:
		userInputParticipant = input("- ").strip()
		if userInputParticipant == "":
			break
		else:
			team.append(userInputParticipant)
	teams.insert((teamID - 1), team)
	print(f"Team {teamID} added")

# Function to remove team
def removeTeam():
	print("Give Team ID or Team Name that you wish to remove.")
	userInputRemoveTeam = input("- ")
	for team in teams:
		if userInputRemoveTeam == team[1]:
			print(f"Removing team {team[0]}: {team[1]}")
			teams.remove(team)
			break
		else:
			try:
				userInputRemoveTeam = int(userInputRemoveTeam)
				if userInputRemoveTeam == team[0]:
					print(f"Removing team {team[0]}: {team[1]}")
					teams.remove(team)
					break
			except:
				continue
		print("No team found")

# Print teams function
def printTeams():
	output = []
	print("Teams:")
	for team in teams:
		print(f"{team[0]}: {team[1]}: ", end="")
		for member in team[3:]:
			output.append(member)
		print(", ".join(output))
		output = []

def main():
	# Create list of all team IDs
	teamIDs = []
	missingTeamIDs = []
	for team in teams:
		teamIDs.append(team[0])
	
	for number in range(1, (len(teamIDs) + 2)):
		if number not in teamIDs:
			missingTeamIDs.append(number)
	
	global totalTeams
	userInputCommand = input("> ").lower()
	
	output = []
	
	if userInputCommand == "help":
		commandHelp()
	
	elif userInputCommand == "exit":
		print("Exiting...")
		exit()
	
	elif userInputCommand == "addteam":
		totalTeams += 1
		addTeam(missingTeamIDs[0])
		missingTeamIDs.pop(0)
	
	elif userInputCommand == "removeteam":
		printTeams()
		removeTeam()
	
	elif userInputCommand == "teams":
		printTeams()
	
	elif userInputCommand == "teamsraw":
		print(teams)
	
	elif userInputCommand == "events":
		print("Team events: ")
		for event in teamEvents:
			output.append(event)
		print(", ".join(output))
		
		output = []
		
		print("Individual events: ")
		for event in individualEvents:
			output.append(event)
		print(", ".join(output))

	else:
		print("Invalid command given.")

# Run script if script is run specifically
if __name__ == "__main__":
	while True:
		main()
