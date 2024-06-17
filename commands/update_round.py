from commands.context import Context

from .base import BaseCommand


class RoundUpdateCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, tournament, round, **data):
        self.tournament = tournament
        self.round = round

    def execute(self):
        self.tournament = self.tournament.next_round()
        return Context("tournament-view", tournament=self.tournament)