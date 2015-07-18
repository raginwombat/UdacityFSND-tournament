#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database.
        Also Modifies the player records =0 since there are no matches
        Requires: player_record and matches Tables exist
        Gets: Nothing
        Modifies: Wins and losses for players 0, removes all matches"""
    DB= connect()
    c = DB.cursor()
    c.execute('delete from matches *;')
    c.execute('update player_records set wins=0,  losses=0 where id  <> Null;')
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database.
        Since there are no players, removing player_recordsd
        and matches to preserve relative integrity
        Requires: Tables, players, player_records and matches exist
        Gets: Nothing
        Modifies: All tables are zeroed out"""
    DB= connect()
    c = DB.cursor()
    
    c.execute('delete from matches  *');
    c.execute('delete from player_records *');
    c.execute('delete from players  *');
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered.
        Requires: 
        Gets: Nothing
        Modifies: """
    DB= connect()
    c = DB.cursor()
    c.execute('select count(*) from players;');
    playersCount = c.fetchone()[0]
    DB.close()
    return playersCount


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
        Requires: 
        Gets: player name
        Modifies: 
        notes make a try and catch for error handlling w/ bd  name"""
    DB= connect()
    c = DB.cursor()
    c.execute('insert into players(name) Values(%s)', (name,) );
    """ Get the player ID number for initializing the player record"""
    c.execute ('select id from players where name = %s', (name, ))
    player_id = c.fetchone()
    c.execute('insert into player_records values( %s , 0, 0)', (player_id[0], ))
    DB.commit()
    DB.close()


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
         Requires: 
        Gets: Nothing
        Modifies: """
    DB= connect()
    c = DB.cursor()

    query = '''select players.id,name, player_records.wins, (player_records.wins + player_records.losses) as matches
            from (players full join player_records on players.id = player_records.id);'''
    c.execute(query);
    standing =c.fetchall()
    DB.close()
    return standing


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      Requires:  Winer and Loser be registered players in the competition
        Gets: Nothing
        Modifies: 

        notes make a try and catch for error handlling w/ bd ID number"""
    DB= connect()
    c = DB.cursor()
    """ Get win and loss, increment for player
        check if player exists, if doesn't then insert"""
    ''' To build out, if the player does not exist register them.'''

    query1 = '''insert into matches(winner, loser) 
                Values(%s, %s);'''
    
    
    c.execute(query1, (winner,loser));
    DB.commit()
    updatePlayerRecords(winner, loser)

    DB.close()
 
 
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
       Requires: 
        Gets: Nothing
        Modifies: """
    DB= connect()
    c = DB.cursor()
    c.execute('''select players.id, players.name
                from players
                join player_records on players.id = player_records.id
                order by player_records.wins desc;''')

    matches = c.fetchall();
    pairings = list()
 
    for  x in range(0, len(matches),2):
        pairings.append( (list(matches[x])+ list(matches[x+1])) )

    DB.close()
    return pairings


def updatePlayerRecords(winner, loser):
    '''Winner player reocrd update
        Requires: This libary requires players to be registerd and to have matches
        for the player reocrd to be updated correcly
    '''    


    DB= connect()
    c = DB.cursor()

    
    query1 = '''update player_records
                set
                    wins = (select count(winner) from matches where winner = %s),
                    losses = (select count(loser) from matches where loser = %s)
                where id = %s;'''

    '''loser player record update'''
    query2 =  '''update player_records
                set
                    wins = (select count(*) from matches where winner = %s),
                    losses = (select count(*) from matches where loser = %s)
                where id = %s;'''
    c.execute(query1, (winner, winner, winner));
    c.execute(query2, (loser, loser, loser));
    DB.commit()
    DB.close()



def playerExists(id):
    DB = psychopg2.connect("dbname=tournament")
    c=DB.cursor()

    c.execute('''select name  from players where id = %s''', (id,))
    if (c.fetchone() != 0 ):
        return false
    else:
        return true
'''
Stub to implmenet OMW 
def OMW(player_id):
    '''select the player and sum all of the  wins from  oponent'''
    DB =  connect()
    
    oponents 
'''