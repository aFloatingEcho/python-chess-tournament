import json
from pathlib import Path

from .tournament import Tournament


class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.tournaments.append(Tournament(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def create(self, name, dates, venue, number_of_rounds):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tours = Tournament(name=name, filepath=filepath, dates=dates,
                           venue=venue, number_of_rounds=number_of_rounds)
        tours.save()

        self.tournaments.append(tours)
        return tours
