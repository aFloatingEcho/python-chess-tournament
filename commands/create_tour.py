from commands.context import Context
from models import TournamentManager

from .base import BaseCommand


class TournamentCreateCmd(BaseCommand):
    """Command to create a tournament."""

    def __init__(self, name, dates, venue, number_of_rounds):
        self.name = name
        self.dates = dates
        self.venue = venue
        self.number_of_rounds = number_of_rounds

    def execute(self):
        """Uses a Tournament instance to create the tournament and add it to the list of tours"""
        tm = TournamentManager()
        tour = tm.create(name=self.name, dates=self.dates,
                         venue=self.venue, number_of_rounds=self.number_of_rounds)
        return Context("tournament-view", tournament=tour)
