from commands import EditTourCmd, NoopCmd

from ..base_screen import BaseScreen


class TournamentEdit(BaseScreen):
    """Screen displayed when editing a player (creating or changing an existing one)"""

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        while True:
            print("Type 'E' to edit add a player, or 'B' to return to tournament view.")
            action = self.input_string()
            if action.upper() == "B":
                return NoopCmd("tournament-view", tournament=self.tournament)
            elif action.upper() == "E":
                player = ""
                return NoopCmd("tournament-edit", tournament=self.tournament, player=player)