from commands import ExitCmd, NoopCmd

from .base_screen import BaseScreen


class MainMenuTour(BaseScreen):
    """Main menu screen for tournaments"""

    def __init__(self, tournaments):
        self.tournaments = tournaments

    def display(self):
        for idx, tournaments in enumerate(self.tournaments, 1):
            print(idx, tournaments.name)

    def get_command(self):
        while True:
            print("Type C to create a tournament or a tournament number to view/edit it.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.tournaments) + 1):
                    return NoopCmd("tournament-view", tournament=self.tournaments[value - 1])
            elif value.upper() == "C":
                return NoopCmd("tournament-create")
            elif value.upper() == "X":
                return ExitCmd()
