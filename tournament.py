#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    return (DB, c)


def deleteMatches():
    """Remove all the match records from the database.
        Also Modifies the player records =0 since there are no matches
        Requires: player_record and matches Tables exist
        Gets: Nothing
        Modifies: Wins and losses for players 0, removes all matches"""
    (DB,c) = connect()
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
    (DB,c) = connect()
    
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
    (DB, c)= connect()
    
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
    (DB,c) = connect()
    c.execute('insert into players(name) Values(%s)', (name,) );
    """ Get the player ID number for initializing the player record"""
    c.execute ('select id from players where name = %s', (name, ))
    player_id = c.fetchone()
    '''Sql Query:
    This query inputs a players record into the Player Record table
    with the format for the table being ID | Wins | Losses.
    Since a new player doesn't have any wins or loses they are set to
    0 to initialize them
     '''
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
    (DB,c) = connect()

    query = ''' select * from standingsQuery;'''
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
    (DB,c) = connect()
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
    (DB,c) = connect()

   
    ''' swissQeuery returns a list of all players ranked by the number of wins.
    This ranked ordering is then used to pair up set of players for a match
    The Query is build by pulling Player ID and Name from the player table,
    the number of wins are then used to sort the player ID and Name.
    Note the Player windows are not actually returned as part of query.
    '''
    c.execute('''select * from swissQuery;''')

    matches = c.fetchall();
    pairings = list()
    '''Check For Odd Number of Playser'''
    if (countPlayers() % 2 == 1 ) :

        ''''If there are an odd number of players check to see if the person in last place
        has gotten a Bye skip. if so  move to teh 2nd to last player.
        If everyone has a skip then give it to the last person. '''''
        
        c.execute(''' select player_ID from  byeStandings;''')
        skippedPlayers = c.fetchall()
        for player in pairings:
            if player not in skippedPlayers:
                '''If the player doesn't have a bye skip they get one '''
        

    else:
     
        for  x in range(0, len(matches),2):
            pairings.append( (list(matches[x])+ list(matches[x+1])) )

    DB.close()
    return pairings


def updatePlayerRecords(winner, loser):
    '''Winner player reocrd update
        Requires: This libary requires players to be registerd and to have matches
        for the player reocrd to be updated correcly
    '''    


    (DB,c) = connect()

    
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
    (DB,c) = connect()

    c.execute('''select name  from players where id = %s''', (id,))
    if (c.fetchone() != 0 ):
        DB.close()
        return false
    else:
        DB.close()
        return true
'''
Stub to implmenet OMW '''
def OMW(player_id):
    '''select the player and sum all of the  wins from  oponent'''
    (DB, c) =  connect()

    DB.close()
    

def getPlayerID(name):
    '''This function returns the ID of the player specifed'''
    (DB, c) = connect()
    try:
        c.execute ('''select id from players where name = %s''', (name, ))
        player_id = c.fetchone()
    
    except Execption:
        return null

    return player_id


def byeSkipped(player_id):
    '''This Method checks to see if a player has received a Bye pass 
    due to an odd number of players. If they have the method returns true. 
    Otherwise it reutnrs false
    Bye skips are recorded by having the Match table have no entry for a winner
    Requires: No special requirements

    '''
    (DB, c) =connect()

    c.execute('''select winner from player_record where loser IS NULL''' )
    oddMan = c.fetchall;

    for x in oddMan:
        if(x == player_id):
            return true
        else:
            return false



def countWins(player_id):
        '''Count the wins for a player'''