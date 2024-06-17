from commands import MatchUpdateCmd

from ..base_screen import BaseScreen


class MatchEdit(BaseScreen):
    """Screen displayed when editing a match."""

    def __init__(self, round, tournament, matches=None):
        self.tournament = tournament
        self.round = round
        self.matches = matches

    def get_command(self):
        data = self.matches
        print(self.matches['players'][0], " vs. ", self.matches['players'][1])
        print("Type in F to complete the match. Otherwise, the match is continued.")
        action = self.input_string()
        if (action.upper() == "F"):
            self.matches.update({"completed": True})
            print("Pick a winner based off number, if an invalid value is picked, no winner will be picked.")
            for idx, each in enumerate(self.matches['players']):
                print(idx + 1, " ", each)
            action = self.input_string()
            if (action.isdigit()):
                action = int(action) - 1
                if (action == 0 or action == 1):
                    self.matches.update({"winner": self.matches['players'][action]})
            else:
                self.matches.update({"winner": None})

        return MatchUpdateCmd(self.tournament, self.round, self.matches, **data)
