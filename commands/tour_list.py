from commands.context import Context
from models import TournamentManager

from .base import BaseCommand


class TourListCmd(BaseCommand):
    """Command to get the list of clubs"""

    def execute(self):
        tm = TournamentManager()
        return Context("main-menu-tour", tournaments=tm.tournaments)