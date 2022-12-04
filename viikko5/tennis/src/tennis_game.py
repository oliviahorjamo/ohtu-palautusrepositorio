class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_names = ['Love', 'Fifteen', 'Thirty', 'Forty', 'Deuce']

    def add_point_for_winner(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def tie_score(self):
        if self.m_score1 == self.m_score2:
            return True
        return False

    def tie_score_str(self):
        if self.m_score1 < 4:
            tie_point = self.score_names[self.m_score1]
            return f'{tie_point}-All'
        return self.score_names[4]

    def advantage_score(self):
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return True
        return False

    def whose_advantage(self):
        player1_difference = self.m_score1 - self.m_score2
        if player1_difference > 0:
            return 1
        return 2

    def win(self):
        point_difference = abs(self.m_score1 - self.m_score2)
        if point_difference > 1:
            return True
        return False

    def advantage_str(self, winner):
        return f'Advantage player{winner}'

    def win_str(self, winner):
        return f'Win for player{winner}'


    def get_score(self):
        score = ""
        temp_score = 0

        if self.tie_score():
            score = self.tie_score_str()

        elif self.advantage_score():

            advantage_holder = self.whose_advantage()

            if self.win():
                score = self.win_str(advantage_holder)
            else:
                score = self.advantage_str(advantage_holder)

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
