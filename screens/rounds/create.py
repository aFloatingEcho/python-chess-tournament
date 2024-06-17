from commands import RoundUpdateCmd, NoopCmd

from ..base_screen import BaseScreen


class CreateRound(BaseScreen):
    """Screen displayed when setting up another round."""
    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        """Goes through the attributes and gets them from the user"""
        print("Are you sure you want move on with the tournament?")
        print("Type in 'Y' (without quotes) to confirm.")
        value = self.input_string()
        if (value.upper() == "Y" and len(self.tournament.players) >= 2):
            return RoundUpdateCmd(tournament=self.tournament)
        if (len(self.tournament.players) < 2):
            print("You need more players before starting the tournament.")
        return NoopCmd("tournament-view", tournament=self.tournament)
