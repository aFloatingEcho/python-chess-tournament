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
        print("Round Information:")
        if (self.tournament.current_round == None):
            print("Tournament has finished.")

        else:
            print("Current Round Information:")
            for idx, each in enumerate(self.tournament.rounds[self.tournament.current_round - 1], 1):
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
        """Gets the command for this screen"""
        while True:
            print("Viewing tournament.")
            value = self.input_string()
            if value.upper() == "B":
                return TourListCmd()
            elif value.isdigit() and (self.tournament.current_round != None):
                value = int(value)
                return NoopCmd(
                    "match-edit", tournament=self.tournament, 
                    match=self.tournament.rounds[self.tournament.current_round - 1][value - 1]
                )