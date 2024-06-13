from commands.context import Context
from models import TournamentManager

from .base import BaseCommand

class TournamentCreateCmd(BaseCommand):
    """Command to create a tournament."""

    def __init__(self, name):
        self.name = name

    def execute(self):
        """Uses a Tournament instance to create the tournament and add it to the list of tours"""
        tm = TournamentManager()
        tour = tm.create(self.name)
        return Context("tournament-view", tour=tour)