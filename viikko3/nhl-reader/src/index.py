import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []

    def find_players(self):
        response = requests.get(self.url).json()

        #print("JSON-muotoinen vastaus:")
        #print(response)

        for player_dict in response:
            player = Player(
                player_dict
            )

            self.players.append(player)

        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.find_players()

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)
        
        newlist = sorted(players, key=lambda p: p.goals + p.assists, reverse=True)
        return newlist


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    player_reader = PlayerReader(url)
    stats = PlayerStats(player_reader)
    fin_players = stats.top_scorers_by_nationality('FIN')

    for player in fin_players:
        print(player)



if __name__ == "__main__":
    main()
