#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def makeQuery(Query,withRet=0):
        conn = connect()
        c = conn.cursor()
        c.execute(Query)
        

        if withRet == 0 :
            conn.commit()
            conn.close()
            
        else :
            ret = c.fetchall()
            conn.close()
            return ret


        
    
   

def deleteMatches():
    """Remove all the match records from the database."""
    makeQuery("DELETE FROM matches")
    




def deletePlayers():
    """Remove all the player records from the database."""
    makeQuery("DELETE FROM players")


def countPlayers():
    """Returns the number of players currently registered."""
    return makeQuery("SELECT count(*) FROM players",1)[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO players(name) VALUES(%s)", (name,))
    conn.commit()
    conn.close()


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
    return makeQuery("SELECT * FROM standings ORDER BY wins DESC",1)

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost


    """





    conn = connect()
    c = conn.cursor()
    # add match to table
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s,%s)", (winner, loser))
    # winner gains a victory and adds to match total

    conn.commit()
    conn.close()

    

    

 
 
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
    players=playerStandings()
    pairs=[]
    if len(players) % 2 == 0:
        for i in range(0, len(players), 2):
            pair = (players[i][0], players[i][1], players[i+1][0], players[i+1][1])
            pairs.append(pair)

    return pairs
        # for i in range(len(players)-1):
        #      print [[i], a[i+1]]



if __name__ == '__main__':

    # print(countPlayers())

    # deleteMatches()
    # deletePlayers()

    # registerPlayer("ahmed")
    # # print(countPlayers())
    # registerPlayer("maahmed")
    # print(countPlayers())

    #print(reportMatch(2,1))
    # print(swissPairings())
    #print(makeQuery("Select * from matches ",1))
    print ("--------------------")
    print(playerStandings())
    # print(countPlayers())

    # print(countPlayers())

    print(reportMatch(1,2))
    print(reportMatch(1,2))
    print(reportMatch(1,2))
    print(reportMatch(1,2))
    print(swissPairings())
    # print(makeQuery("Select * from matches ",1))
    print ("--------------------")
    print(playerStandings())




