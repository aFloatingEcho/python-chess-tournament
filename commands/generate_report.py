from commands.context import Context

from .base import BaseCommand


class GenerateReport(BaseCommand):
    """Command to handle matches"""

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        self.tournament.generate_report()
        return Context("tournament-view", tournament=self.tournament)