import json

from .match import Match

class Tournament:
    """
    A local tournament.

    Data is loaded from a JSON file (provided as arguement).
    The class creates round information based off JSON info.
    """

    def __init__(self, filepath=None, name=None):
        """
        The constructor works in two ways:
        - if filepath is provided, it loads data from JSON
        - if it is not but a name is provided, it creates a new tournament
        (and a new JSON file)
        """

        self.name = name
        self.filepath = filepath
        self.matches = []

        if filepath and not name:
            # Load data from the JSON file
            with open(filepath) as fp:
                data = json.load(fp)
                self.name = data["name"]
                # self.dates
                self.venue = data["venue"]
                self.number_of_rounds = data["number_of_rounds"]
                self.current_round = data["current_round"]
                self.completed = data["completed"]
                self.players = data["players"]
                self.finished = data.get("finished")
                # self.rounds
        elif not filepath:
            # We did not have a file, so we are going to create it by running the save method
            self.save()

    def save(self):
        """Serialize the tournament into JSON format for storage."""

        with open(self.filepath, "w") as fp:
            json.dump(
                {"name": self.name, "dates": self.dates, "venue": self.venue,
                "number_of_rounds": self.number_of_rounds, "current_round": self.current_round, "completed": self.completed,
                "players": self.players, "finished": self.finished, "rounds": self.rounds},
            fp,
            )

            