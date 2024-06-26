from commands import TourListCmd
from screens import TournamentCreate, TournamentView, MainMenuTour, MatchEdit
from screens import MatchView, ViewRound, CreateRound, TournamentEdit


class App:
    """The main controller for the tournament management program"""

    SCREENS = {
        "main-menu-tour": MainMenuTour,
        "tournament-create": TournamentCreate,
        "tournament-view": TournamentView,
        "match-edit": MatchEdit,
        "match-view": MatchView,
        "round-view": ViewRound,
        "round-create": CreateRound,
        "tournament-edit": TournamentEdit,
        "exit": False,
    }

    def __init__(self):
        # We start with the list of tournaments (= main menu)
        command = TourListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            # Get the screen class from the mapping
            screen = self.SCREENS[self.context.screen]
            try:
                # Run the screen and get the command
                command = screen(**self.context.kwargs).run()
                # Run the command and get a context back
                self.context = command()
            except KeyboardInterrupt:
                # Ctrl-C
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = App()
    app.run()
