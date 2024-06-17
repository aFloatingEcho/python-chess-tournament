from commands.context import Context

from .base import BaseCommand


class RoundUpdateCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, tournament, round, match, **data):
        self.tournament = tournament
        self.round = round

    def execute(self):
        return Context("tournament-view", tournament=self.tournament, round=self.round)