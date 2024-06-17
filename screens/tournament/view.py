from commands import TourListCmd, NoopCmd, GenerateReport

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
        if (self.tournament.current_round is None):
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
            print("Press 'G' to generate a report of the tournament.")
            if (self.tournament.current_round is not None):
                print("Press 'E' to edit the current round.")
                print("Press 'A' to advance the tournament.")
                print("Press 'R' to register a new player.")
            value = self.input_string()
            if value.upper() == "B":
                return TourListCmd()
            elif value.upper() == "G":
                return GenerateReport(tournament=self.tournament)
            elif value.upper() == "E" and (self.tournament.current_round is not None):
                return NoopCmd(
                    "round-view", tournament=self.tournament,
                    matches=self.tournament.rounds[int(self.tournament.current_round) - 1]
                )
            elif value.upper() == "A" and (self.tournament.current_round is not None):
                return NoopCmd(
                    "round-create", tournament=self.tournament
                )
            elif value.upper() == "R" and (self.tournament.current_round is not None):
                return NoopCmd(
                    "tournament-edit", tournament=self.tournament
                )
