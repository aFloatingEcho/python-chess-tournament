from .match import Match


class Round:

    def __init__(self, matches):
        self.matches = matches

    def __str__(self):
        stringToReturn = ""
        for each in self.matches:
            stringToReturn += (str(each) + "/n")
        return stringToReturn

    def serialize(self):
        """Serialize the rounds into JSON format for storage"""
        data = {attr: getattr(self, attr) for attr in ("matches")}
        return data

    def create_match(self, **kwargs):
        match = Match(**kwargs)
        self.matches.append(match)
        self.serialize()
        return match

    def update_match(self, match, **kwargs):
        if match not in self.matches:
            raise RuntimeError("Match not in database")

        for key, value in kwargs.items():
            setattr(match, key, value)

        self.serialize()
        return match

    def checkIfRoundIsCompleted(self):
        for each in self.matches:
            if not (each.getMatchStatus()):
                return False
        return True
