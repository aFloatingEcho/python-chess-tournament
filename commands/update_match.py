from commands.context import Context
from models import Match

from .base import BaseCommand

class MatchHandleCmd(BaseCommand):
    """Command to handle matches"""

    def __init__(self, players, completed, winner, **data):
        self.players = players
        self.completed = completed
        self.winner = winner
        self.data = data
