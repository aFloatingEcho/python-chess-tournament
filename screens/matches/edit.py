from commands import MatchUpdateCmd

from ..base_screen import BaseScreen


class MatchEdit(BaseScreen):
    """Screen displayed when editing a match."""

    def __init__(self, tournament, match=None):
        self.tournament = tournament
        self.match = match

    def get_command(self):

        return MatchUpdateCmd(self.tournament, self.match)