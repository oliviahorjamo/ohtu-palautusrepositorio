from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

  #  matcher = And(
   #     HasAtLeast(5, "goals"),
    #    HasAtLeast(5, "assists"),
     #   PlaysIn("PHI")
    #)


  #  matcher = And(
   # HasAtLeast(70, "points"),
    #Or(
     #   PlaysIn("NYR"),
      #  PlaysIn("FLA"),
       # PlaysIn("BOS")
    #)
#)

    query = QueryBuilder()
    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)

    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))

if __name__ == "__main__":
    main()
