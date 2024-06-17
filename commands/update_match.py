from commands.context import Context

from .base import BaseCommand


class MatchUpdateCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, tournament, round, match, **data):
        self.tournament = tournament
        self.round = round
        self.match = match
        self.data = data

    def execute(self):
        self.tournament.update_match(self.match, **self.data)
        return Context("tournament-view", tournament=self.tournament)
