import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(player_dict) for player_dict in response]

    finns = filter(lambda player: player.nationality == "FIN", players)
    sorted_finns = sorted(finns, key=lambda player: player.points, reverse=True)

    print("Players from FIN")
    for player in sorted_finns:
        print(player)


if __name__ == "__main__":
    main()
