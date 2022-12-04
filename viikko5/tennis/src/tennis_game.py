class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0
        self.score_names = ['Love', 'Fifteen', 'Thirty', 'Forty', 'Deuce']

    def add_point_for_winner(self, player_name):
        if player_name == "player1":
            self.score_player1 = self.score_player1 + 1
        else:
            self.score_player2 = self.score_player2 + 1

    def tie_score(self):
        if self.score_player1 == self.score_player2:
            return True
        return False

    def tie_score_str(self):
        if self.score_player1 < 4:
            tie_point = self.score_names[self.score_player1]
            return f'{tie_point}-All'
        return self.score_names[4]

    def advantage_score(self):
        if self.score_player1 >= 4 or self.score_player2 >= 4:
            return True
        return False

    def whose_advantage(self):
        player1_difference = self.score_player1 - self.score_player2
        if player1_difference > 0:
            return 1
        return 2

    def win_score(self):
        point_difference = abs(self.score_player1 - self.score_player2)
        if point_difference > 1:
            return True
        return False

    def advantage_str(self, winner):
        return f'Advantage player{winner}'

    def win_str(self, winner):
        return f'Win for player{winner}'

    def not_tie_nor_advantage_str(self):
        player1_score_str = self.score_names[self.score_player1]
        player2_score_str = self.score_names[self.score_player2]
        return f'{player1_score_str}-{player2_score_str}'


    def get_score(self):
        score = ""

        if self.tie_score():
            score = self.tie_score_str()

        elif self.advantage_score():

            advantage_holder = self.whose_advantage()

            if self.win_score():
                score = self.win_str(advantage_holder)
            else:
                score = self.advantage_str(advantage_holder)

        else:
            score = self.not_tie_nor_advantage_str()
            
        return score
