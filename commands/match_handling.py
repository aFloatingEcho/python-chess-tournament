from commands.context import Context
from models import match

from .base import BaseCommand

class MatchHandleCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, players, completed, winner):
        self.players = players
        self.completed = completed
        self.winner = winner