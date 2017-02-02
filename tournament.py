#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name = "tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to {}".format(database_name))
    #-----Done-----#


def deleteMatches():
    """Remove all the match records from the database."""
    conn, cur = connect()

    cur.execute("TRUNCATE matches RESTART IDENTITY;")
    
    conn.commit()
    conn.close()
    #-----Done-----#


def deletePlayers():
    """Remove all the player records from the database."""
    conn, cur = connect()

    cur.execute("TRUNCATE players RESTART IDENTITY CASCADE;");
    
    conn.commit()
    conn.close()
    #-----Done-----#


def countPlayers():
    """Returns the number of players currently registered."""
    conn, cur = connect()

    cur.execute("SELECT COUNT(*) FROM players;")
    total_registered_players = cur.fetchone();
    conn.close()
    
    return total_registered_players[0]
    #-----Done-----#


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn, cur = connect()
    
    query = "INSERT INTO players (name) VALUES (%s)"
    params = (name,)
    cur.execute(query, params)
    
    conn.commit()
    conn.close()
    #-----Done-----#


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, cur = connect()

    cur.execute('''SELECT p.id, p.name,
                 (SELECT COUNT(*) FROM matches m1 WHERE p.id = m1.winner) AS wins,
                 (SELECT COUNT(*) FROM matches m2 WHERE p.id = m2.winner OR p.id = m2.loser) AS total_matches
                 FROM players AS p
                 ORDER BY wins DESC;''')

    standings = cur.fetchall()
    
    conn.close()
    
    return standings
    #-----Done-----#



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, cur = connect()

    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
    params = (winner, loser,)
    cur.execute(query, params)
    
    conn.commit()
    conn.close()
    #-----Done-----#
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    standing_index = 0
    pair_index = 0
    pairings = []

    while standing_index < len(standings):
        pair = standings[standing_index][0:2] + standings[standing_index+1][0:2]
        pairings.insert(pair_index, pair)
        standing_index += 2
        pair_index += 1

    return pairings
    #-----Done-----#

