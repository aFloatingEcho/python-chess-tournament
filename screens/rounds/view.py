from commands import NoopCmd

from ..base_screen import BaseScreen


class ViewRound(BaseScreen):
    """Screen displayed when viewing a round."""

    def __init__(self, tournament, matches):
        self.tournament = tournament
        self.matches = matches

    def display(self):
        print("Currently Viewing Round " + str(self.tournament.current_round))
        for idx, each in (enumerate(self.matches, 1)):
            print("Match " + str(idx))
            print(each["players"][0] + " vs " + each["players"][1])
            if(each["completed"]):
                if(each["winner"] == None):
                    print("The match concluded with no winner.")
                else:
                    print("The match concluded with " + each["winner"] + "as the winner.")
            else:
                print("The match is ongoing.")

    def get_command(self):
        """Gets the command for this screen."""
        while True:
            value = self.input_string()
            if value.upper() == "B":
                return NoopCmd("tournament-view", tournament=self.tournament)
            # elif value.isdigit() and (self.view_round_no == (self.tournament.current_round - 0)):
