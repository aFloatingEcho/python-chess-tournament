from .match import Match


class Round:
    
    def __init__(self, matches):
        self.matches = matches

    def serialize(self):
        """Serialize the rounds into JSON format for storage"""
        data = {attr: getattr(self, attr) for attr in ("matches")}
        return data

    def getMatch(self, no):
        return self.matches[no]
    
    def checkIfRoundIsCompleted(self):
        for each in self.matches:
            if not (each.getMatchStatus()):
               return False
        return True