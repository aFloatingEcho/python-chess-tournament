
class Match:
    """
    The match class contains information about a chess match.
    """

    def __init__(self, players, completed, winner):
        self.player1 = players
        self.completed = completed
        self.winner = winner

    def __str__(self):
        match_info = str(self.player1) + " vs. " + str(self.player2)
        return match_info

    def setCompleted(self, status):
        self.completed = status

    def setWinner(self, winner):
        if(self.players.include(winner)):
            self.winner = winner
        else:
            print("A winner has to be from the two players.")

    def serialize(self):
        """Serialize the match into JSON format for storage."""
        data = {attr: getattr(self, attr) for attr in ("player1", "player2", "completed", "winner")}
        return data
