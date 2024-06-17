from commands import EditTourCmd, NoopCmd
from models import ClubManager

from ..base_screen import BaseScreen


class TournamentEdit(BaseScreen):
    """Screen displayed when editing a player (creating or changing an existing one)"""

    def __init__(self, tournament):
        self.tournament = tournament
        self.cm = ClubManager()
        self.players = []
        for each_club in self.cm.clubs:
            for every_player in each_club.players:
                self.players.append(every_player)
        for each in self.players:
            print(each.name, " ", each.chess_id)

    def get_command(self):
        while True:
            print("Type 'E' to add a player, or 'B' to return to tournament view.")
            action = self.input_string()
            if action.upper() == "B":
                return NoopCmd("tournament-view", tournament=self.tournament)
            elif action.upper() == "E":
                print("Type 'N' to attempt to add a player by name.")
                print("Type 'I' to add a player by ID.")
                action = self.input_string()
                if (action.upper() == "N"):
                    print("Input name.")
                    print("Warning: Function will pick first name on the list.")
                    action = self.input_string()
                    for each in self.players:
                        if (action in each.name):
                            print("Adding: ", each.name, " ", each.chess_id)
                            return EditTourCmd(tournament=self.tournament, player=each.chess_id)
                elif (action.upper() == "I"):
                    action = self.input_chess_id()
                    for each in self.players:
                        if (action == (each.chess_id)):
                            print("Adding: ", each.name, " ", each.chess_id)
                            return EditTourCmd(tournament=self.tournament, player=each.chess_id)
            return NoopCmd(
                    "tournament-edit", tournament=self.tournament
                )
