
class Round:
    
    def __init__(self, matches):
        self.matches = matches
    
    def serialize(self):
        """Serialize the rounds into JSON format for storage"""
        data = {attr: getattr(self, attr) for attr in ("matches")}
        return data