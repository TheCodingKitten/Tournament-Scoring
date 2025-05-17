#!/usr/bin/env python3

# Tournament Scoring and Management
# Created by Henry Nevill
# https://github.com/TheCodingKitten/Tournament-Scoring/

import csv

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
teamsFormat = ["Team ID", "Team Name", "Score", "Member Names"]
teams = []

totalTeams = 0

# Function to add team and members
def addTeam(teamID):
	print("Adding team. Enter a blank value to stop adding members.")
	team = [teamID]
	team.append(input("Team name: "))
	team.append(0)
	print("Add team member names: ")
	teamMembers = []
	while True:
		userInputParticipant = input("- ").strip()
		if userInputParticipant == "":
			break
		else:
			teamMembers.append(userInputParticipant)
	team.append(teamMembers)
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

# Print teams function
def printTeams():
	output = []
	print("Teams:")
	for team in teams:
		print(f"{team[0]}: {team[1]}: ", end="")
		for member in team[3]:
			output.append(member)
		print(", ".join(output))
		output = []

# Import from CSV file
def importFromCSV(filename):
	global teams
	
	if filename == "": # Check if filename blank
		filename = "example.csv" # Set default filename
	
	if teams != []:
		print("Current teams list is not empty, continuing will overwrite current teams.")
		userInputContinue = input("Type Y to continue, anything else to cancel: ").lower()
		if userInputContinue != "y":
			print("Cancelling import")
			return # Stop function
	
	print(f"Importing from {filename}")
	
	with open(filename, newline="") as csvFile:
		fileReader = csv.reader(csvFile, dialect="excel")
		output = []
		for row in fileReader:
			entryOutput = []
			for entry in row:
				entryOutput.append(entry)
			output.append(entryOutput)
		output.pop(0) # Removes header line
		
		# Convert teamIDs to int
		for team in output:
			team[0] = int(team[0])
		
		# Replace string of names with list
		for team in output:
			team[3] = team[3].split(",")
	
	numImported = len(output)
	print(f"Imported {numImported} teams from {filename}")
	
	teams = output

# Export to CSV file
def exportToCSV(filename):
	if filename == "": # Check if filename blank
		filename = "writeexample.csv" # Set default filename
	
	print(f"Exporting to {filename}")
	
	with open(filename, "w", newline="") as csvFile:
		fileWriter = csv.writer(csvFile, dialect="excel")
		
		fileWriter.writerow(teamsFormat)
		
		for team in teams:
			team[3] = ",".join(team[3])
			print(team[3])
			fileWriter.writerow(team)
		

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
		addTeam(missingTeamIDs[-1])
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

	elif userInputCommand == "import":
		importFromCSV(input("Filename: "))

	elif userInputCommand == "export":
			exportToCSV(input("Filename: "))

	else:
		print("Invalid command given.")

# Run script if script is run specifically
if __name__ == "__main__":
	commandHelp()
	while True:
		main()
