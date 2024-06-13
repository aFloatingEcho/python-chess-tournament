from commands import TourListCmd, NoopCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed while viewing a tournament."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("##", self.tournament.name)
        print("###", self.tournament.dates)
        print("Venue:", self.tournament.venue)
        print("Number of Rounds:", self.tournament.number_of_rounds)
        print("Current Round:", self.tournament.current_round)

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            print("Viewing tournament.")
            value = self.input_string()
            if value.upper() == "B":
                return TourListCmd()
            elif value.upper() == "C":
                return NoopCmd("tournament-create", tournament=self.tournament)