from commands import MatchUpdateCmd

from ..base_screen import BaseScreen


class MatchEdit(BaseScreen):
    """Screen displayed when editing a match."""

    def __init__(self, round, tournament, matches=None):
        self.tournament = tournament
        self.round = round
        self.matches = matches

    def get_command(self):
        data = self.matches
        print(str(self.round))
        print(str(data))
        matches = self.tournament.update_match(self.matches, **data)
        return MatchUpdateCmd(self.tournament, self.round, self.matches, **data)