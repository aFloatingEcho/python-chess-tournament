from commands import NoopCmd

from ..base_screen import BaseScreen


class MatchView(BaseScreen):
    """Screen displayed when viewing a Match."""

    def __init__(self, players, completed, winner):
        self.players = players
        self.completed = completed
        self.winner = winner

    def display(self):
        print(str(self))
        if (self.winner is not None):
            print("The match has a winner!")
            print("The winner is: ", self.winner)
        else:
            print("The match currently has no winner.")
        if (self.completed):
            print("The match is concluded.")
        else:
            print("The match is ongoing.")

    def get_command(self):
        while True:
            print("Current match in progress:")
            self.display(self)
            action = self.input_string()
            if action.upper() == "E":
                return NoopCmd("club-view", club=self.club)
