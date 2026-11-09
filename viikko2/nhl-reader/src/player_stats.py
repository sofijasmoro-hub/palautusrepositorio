class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        players = filter(lambda player: player.team == team, self.players)
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä.
        """
        return sorted(self.players, key=lambda player: player.goals, reverse=True)[:how_many]
