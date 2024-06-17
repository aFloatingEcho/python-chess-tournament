from commands import NoopCmd

from ..base_screen import BaseScreen


class MatchView(BaseScreen):
    """Screen displayed when viewing a Match."""

    def __init__(self, tournament, match):
        self.tournament = tournament
        self.match = match

    def display(self):
        print(str(self.match))
        if (self.match['completed']):
            print("The match is concluded.")
            if (self.match.get('winner') is None):
                print("The match ended in a stalemate.")
            else:
                print("The match has a winner!")
                print("The winner is: ", self.match['winner'])
        else:
            print("The match is ongoing.")

    def get_command(self):
        while True:
            print("Current match in progress:")
            self.display()
            return NoopCmd("tournament-view", tournament=self.tournament)
