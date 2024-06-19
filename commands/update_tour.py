from commands.context import Context

from .base import BaseCommand


class EditTourCmd(BaseCommand):
    """Command to add players to a tournament."""

    def __init__(self, tournament, player, **data):
        self.tournament = tournament
        self.player = player

    def execute(self):
        self.tournament.add_player(player=self.player)
        return Context("tournament-view", tournament=self.tournament)
