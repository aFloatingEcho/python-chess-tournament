

class Tournament:

    def __init__(self, name, dates, venue, number_of_rounds, current_round, completed, players, finished, rounds):
        self.name = name
        self.dates = dates
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed
        self.players = players
        self.finished = finished
        self.rounds = rounds

    def serialize(self):
        """Serialize the tournament into JSON format for storage."""
        data = {attr: getattr(self, attr) for attr in (
            "name", "dates", "venue",
            "number_of_rounds", "current_round", "completed",
            "players", "finished", "rounds")}
        return data
