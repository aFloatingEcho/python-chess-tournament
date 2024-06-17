from commands import TournamentCreateCmd

from ..base_screen import BaseScreen


class TournamentCreate(BaseScreen):
    """Screen displayed when creating a tournament"""

    display = "## Create tournament"

    def get_command(self):
        print("Type in the name of the tournament")
        name = self.input_string()

        return TournamentCreateCmd(name)
