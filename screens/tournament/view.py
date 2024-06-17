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

    def get_standings(self):
        # Function to obtain the current standings. Note that this is like extremely inefficient.
        standings = {}
        for each in self.tournament.players:
            standings[each] = 0.0
        for each_round in self.tournament.rounds:
            for each_match in each_round:
                if(each_match['completed']):
                    if(each_match['winner'] is not None):
                        standings.update({each_match['winner']: standings.get(each_match['winner']) + 1.0}) 
                    else:
                        standings.update({each_match['players'][0] : standings.get(each_match['players'][0]) + .5})
                        standings.update({each_match['players'][1] : standings.get(each_match['players'][1]) + .5})
        # This particular line is due to this: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        sorted_standings = sorted(standings.items(), key=lambda x:x[1], reverse=True)
        standings = dict(sorted_standings)
        return standings

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            current_standings = self.get_standings()
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