from commands.context import Context

from .base import BaseCommand


class MatchUpdateCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, tournament, match, **data):
        self.tournament = tournament
        self.match = match


    def execute(self):
        return Context("match-view", tournament=self.tournament, match=self.match)