import json
from pathlib import Path

from .tournament import Tournament


class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.clubs = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.clubs.append(Tournament(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        club = Tournament(name=name, filepath=filepath)
        club.save()

        self.clubs.append(club)
        return club
