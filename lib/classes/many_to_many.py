from statistics import mean

class Game:
    def __init__(self, title):
        if isinstance(title, str):
            if len(title) > 0:
                self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self,"_title")==False:
            self._title = new_title

    def results(self):
        return [ result for result in Result.all if result.game == self ]

    def players(self):
        return [ player for player in Player.all if self in player.games_played() ]

    def average_score(self, player):
        if player not in self.players():
            return 0
        else:
            return mean([result.score for result in self.results() if result.player == player])
        

class Player:

    all = []

    @classmethod
    def highest_score(cls, game):
        highest = 0
        current_player = None
        for player in game.players():
            if game.average_score(player) > highest:
                highest = game.average_score(player)
                current_player = player
        return current_player
        

        

    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str):
            if 2 <= len(new_username) <= 16:
                self._username = new_username

    def results(self):
        return [ result for result in Result.all if result.player == self ]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int):
            if 1 <= new_score <= 5000:
                if hasattr(self, "_score")==False:
                    self._score = new_score