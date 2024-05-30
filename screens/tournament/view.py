from commands import NoopCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed while viewing a tournament."""

    def __init__(self, name, dates, venue, number_of_rounds, current_round, completed, players, finished, rounds):
        self.name = name
        self.dates = dates
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed
        self.players = players
        self.finished = finished
        self.rounds = rounds

    def display(self):
        print("##", self.name)
        print("###", self.dates)
        print("Venue:", self.venue)
        print("Number of Rounds:", self.number_of_rounds)
        print("Current Round:", self.current_round)