from commands.context import Context

from .base import BaseCommand


class RoundUpdateCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, tournament, **data):
        self.tournament = tournament

    def execute(self):
        self.tournament.next_round()
        return Context("tournament-view", tournament=self.tournament)