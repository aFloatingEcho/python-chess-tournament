from datetime import datetime


class Match:
    """
    The match class contains information about a chess match.
    """
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, player1, player2, day_of_match):
        self.player1 = player1
        self.player2 = player2
        self.matchPoints = 0

        # Much like how player class handles dates, this line copies how it was written.
        self._match_date = None
        # Match date information
        self.match_date = day_of_match

    def __str__(self):
        return f"<{self.day_of_match}>"

    @property
    def match_date(self):
        """
        Property to get the match day (string) from matchdate (datetime).
        """
        return self.match_date.strftime(self.DATE_FORMAT)

    @match_date.setter
    def match_date(self, value):
        """
        Set the matchdate (datetime) from a string.
        """
        self.match_date = datetime.strptime(value, self.DATE_FORMAT)

    def setMatchPoints(self, value):
        """
        Sets the value of a match.
        """
        self.matchPoints = value

    def serialize(self):
        """Serialize the match into JSON format for storage."""
        data = {attr: getattr(self, attr) for attr in ("player1", "player2", "matchPoints")}
        # As mentioned in player.py, we want to make sure we use
        # the str representation of datetime in JSON.
        data["match_date"] = self.match_date
        return data
