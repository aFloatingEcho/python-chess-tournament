import json
from pathlib import Path

from .tournament import Tournament


class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tours = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.tours.append(Tournament(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tours = Tournament(name=name, filepath=filepath)
        tours.save()

        self.tours.append(tours)
        return tours
