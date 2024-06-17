from commands import TournamentCreateCmd

from ..base_screen import BaseScreen


class TournamentCreate(BaseScreen):
    """Screen displayed when creating a tournament"""

    display = "## Create tournament"

    def get_command(self):
        print("Type in the name of the tournament")
        name = self.input_string()
        print("Type in the starting date of the tournament.")
        start_date = self.input_birthday()
        print("Type in the ending date of the dournament.")
        end_date = self.input_birthday()
        dates = {'from': start_date, 'to': end_date}
        print("Type in the location of the venue.")
        venue = self.input_string()
        print("Type in the number of rounds for the tournament.")
        number_of_rounds = self.input_string()
        number_of_rounds = int(number_of_rounds)

        return TournamentCreateCmd(name=name, dates=dates, venue=venue, number_of_rounds=number_of_rounds)
