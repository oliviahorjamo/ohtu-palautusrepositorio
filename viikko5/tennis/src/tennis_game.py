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
        else:
            return self.score_names[4]


    def get_score(self):
        score = ""
        temp_score = 0

        if self.tie_score():
            score = self.tie_score_str()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
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
