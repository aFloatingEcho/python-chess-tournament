import json


class Tournament:
    """
    A local tournament.

    Data is loaded from a JSON file (provided as arguement).
    The class creates round information based off JSON info.
    """
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, filepath=None,
                 name=None, dates=None, venue=None, number_of_rounds=None):
        """
        The constructor works in two ways:
        - if filepath is provided, it loads data from JSON
        - if it is not but a name is provided, it creates a new tournament
        (and a new JSON file)
        """

        self.filepath = filepath
        self.name = name
        self.dates = dates
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.completed = False
        self.players = []
        self.rounds = []
        self.finished = False

        if filepath and not name:
            # Load data from the JSON file
            with open(filepath) as fp:
                data = json.load(fp)
                self.name = data["name"]
                self.dates = data["dates"]
                self.venue = data["venue"]
                self.number_of_rounds = data["number_of_rounds"]
                self.current_round = data["current_round"]
                self.completed = data["completed"]
                self.players = data["players"]
                self.finished = data.get("finished")
                self.rounds = data.get("rounds")
        elif not filepath:
            # We did not have a file, so we are going to create it by running the save method
            self.save()

    def save(self):
        """Serialize the tournament into JSON format for storage."""

        with open(self.filepath, "w") as fp:
            json.dump({
                "name": self.name, "dates": self.dates, "venue": self.venue,
                "number_of_rounds": self.number_of_rounds, "current_round": self.current_round,
                "completed": self.completed, "players": self.players,
                "finished": self.finished, "rounds": self.rounds},
                fp,
            )

    def update_match(self, match, **kawrgs):
        """Method for updating a particular match in the current match."""

        for each in self.rounds[self.current_round - 1]:
            if match['players'] == each:
                for key, value in match:
                    setattr(each, key, value)

        self.save()
        return match

    def get_standings(self):
        # Function to obtain the current standings. Note that this is like extremely inefficient.
        standings = {}
        for each in self.players:
            standings[each] = 0.0
        for each_round in self.rounds:
            for each_match in each_round:
                if (each_match['completed']):
                    if (each_match['winner'] is not None):
                        standings.update({each_match['winner']: standings.get(each_match['winner']) + 1.0})
                    else:
                        standings.update({each_match['players'][0]: standings.get(each_match['players'][0]) + .5})
                        standings.update({each_match['players'][1]: standings.get(each_match['players'][1]) + .5})
        # This particular line is due to this: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        sorted_standings = sorted(standings.items(), key=lambda x: x[1], reverse=True)
        standings = dict(sorted_standings)
        return standings

    def get_pairings(self):
        standings = list(self.get_standings())
        total_pairings = len(standings) // 2
        pairings = []
        for x in range(total_pairings):
            # if there's more possible combinations, go check if this standing already exists.
            if (len(standings) > 2):
                for each_round in self.rounds:
                    for each_match in each_round:
                        if (each_match['players'] is [standings[0], standings[1]]):
                            pairings.append([standings[0], standings[2]])
                            standings.pop(2)
                            standings.pop(0)
                            continue
                pairings.append([standings[0], standings[1]])
                standings.pop(1)
                standings.pop(0)
            else:
                pairings.append([standings[0], standings[1]])
                standings.pop(1)
                standings.pop(0)
        return pairings

    def next_round(self):
        """Command to begin the next round."""
        pairings = self.get_pairings()
        if (self.current_round < self.number_of_rounds):
            round = []
            for each in pairings:
                round.append({'players': each, 'completed': False, 'winner': None})
            self.current_round += 1
            self.rounds.append(round)
        if (self.current_round == self.number_of_rounds):
            self.completed = True
            self.finished = True
            self.current_round = None
        self.save()
        return self

    def add_player(self, player):
        """Command to add a player. Note sanity check is done elsewhere."""
        if player not in self.players:
            self.players.append(player)
            self.save()
        return player

    def generate_report(self):
        """Command to generate a report, using the name of the tournament on the report."""
        save_location = self.name + ".txt"
        with open(save_location, 'w') as file:
            file.write("Tournament Name: " + self.name + "\n")
            file.write("Tournament Dates:" + self.dates['from'] + " to " + self.dates['to'] + "\n")
            file.write("Tournament Venue:" + self.venue + "\n")
            file.write("Number of Rounds:" + str(self.number_of_rounds) + "\n")
            if (self.current_round is not None):
                file.write("Current Round: " + str(self.current_round) + "\n")
            if (self.completed):
                file.write("The tournament has completed." + "\n")
            players = "Players in tournament: "
            for each in self.players:
                players += each + " "
            file.write(players + "\n")
            for idx, each_round in (enumerate(self.rounds, 1)):
                file.write("## Round " + str(idx) + " -----\n")
                for idy, each_match in (enumerate(each_round, 1)):
                    file.write(">>> Match " + str(idy) + "\n")
                    file.write(each_match["players"][0] + " vs " + each_match["players"][1] + "\n")
                    if (each_match["completed"]):
                        if (each_match["winner"] is None):
                            file.write("The match concluded with no winner." + "\n")
                        else:
                            file.write("The match concluded with " + each_match["winner"] + " as the winner." + "\n")
                    else:
                        file.write("The match is ongoing." + "\n")
        print("Report generated at: \" " + save_location + "\"")
        return self
