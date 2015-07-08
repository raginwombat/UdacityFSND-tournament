  =======================
|Swiss Tournament Library|
 ========================-------------
|   Project 2 subumission by R. Nelson|
 -------------------------------------

 Overview
------------------
 Swiss tournament  is a library that tracks and records siwss tournaments. THe player and records are stored in a postgresql database.


Instructions
------------------
Use the methods defiend in tournmanet.py to start and record  player matches.
 

reportMatch(winner, loser) - 

deleteMatches() - 

playerStandings() - 

swissPairings()


Documentation
------------------

connect():
    Connect to the PostgreSQL database.  Returns a database connection.
 


deleteMatches():
Clear out all the match records from the database.
        Also Modifies the player records =0 since there are no matches
        Requires: player_record and matches Tables exist
        Gets: Nothing
        Modifies: Wins and losses for players 0, removes all matches


 deletePlayers():
 Clear out all the player records from the database.
        Since there are no players, removing player_recordsd
        and matches to preserve relative integrity
        Requires: Tables, players, player_records and matches exist
        Gets: Nothing
        Modifies: All tables are zeroed out

 countPlayers():
 Returns the number of currently registered players. 
        Requires: 
        Gets: Nothing
        Modifies: 


 registerPlayer(name):
    Adds a player to the tournament by putting an entry in the database. The database  assigns an ID number to the player. Different players may have the same names but will receive different ID numbers.
  
  
    Args:
      name: the player's full name (need not be unique).
        Requires: 
        Gets: player name
        Modifies: 
        notes make a try and catch for error handlling w/ bd  name


 playerStandings():
 Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.
    Returns a list of the players and their win records, sorted by wins.

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
        Modifies: 


 reportMatch(winner, loser):
 Stores the outcome of a single match between two players in the database.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      Requires:  Winer and Loser be registered players in the competition
        Gets: Nothing
        Modifies: 

        notes make a try and catch for error handlling w/ bd ID number
 
 
 swissPairings():
    Returns a list of pairs of players for the next round of a match.
  
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
        Modifies: 






Installation
------------------
This library requires a Postgresql database and and Python 2.7 installed locally. THe libraries can be installed using the 
