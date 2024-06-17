from commands import TourListCmd, NoopCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed while viewing a tournament."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("##", self.tournament.name)
        print("###", "From ", self.tournament.dates['from'], " to ", self.tournament.dates['to'])
        print("Venue:", self.tournament.venue)
        print("Number of Rounds:", self.tournament.number_of_rounds)
        print("Current Round:", self.tournament.current_round)
        if (self.tournament.current_round == None):
            print("Tournament has finished.")
        else:
            print("Tournament is ongoing.")

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            current_standings = self.tournament.get_standings()
            print("The tournament standings are as follows:")
            for key, value in current_standings.items():
                print(f"{key}: {value}")
            print("Viewing tournament. Type 'B' to go back.")
            if(self.tournament.current_round is not None):
                print("Press 'E' to edit the current round.")
            value = self.input_string()
            if value.upper() == "B":
                return TourListCmd()
            elif value.upper() == "E" and (self.tournament.current_round != None):
                return NoopCmd(
                    "round-view", tournament=self.tournament,
                    matches=self.tournament.rounds[int(self.tournament.current_round) - 1]
                )