  =======================
|Swiss Tournament Library|
 ========================-------------
|   Project 2 subumission by R. Nelson|
 -------------------------------------

 Overview
------------------
 Swiss tournament  is a library that tracks and records siwss tournaments. THe player and records are stored in a postgresql database.


Requirements
------------------
This library requires that PostGresSQL >= 9.3.7 be installed as well as Python >=2.7.1. A SQL Script has been included to setup the datbase enviromentent for the library to work.
If more instruction is needed on installing or setting up PostGreSQL or Python please refer to their documentation at their websites postgresql.com/docs and python.com/docs.

Instructions
------------------
    Setting up Enviorment
    ------------------
    To setup the enviroment for the tournament app to work please run the Tournament.sql.
    A dtabase named tournament needs to exist for the script to work. If this is the first time you're using this library you can setup the database using thefollowing commands:
    
    $ psql
    daatase=> CREATE DATABASE tournament;
    databasse=> \c tournament;
    You can execute the setup script from the PSQL commandline 
    tournament=> \i tournament.sql;



    If the database is already setup  onlly the setup script needs to be run. To run the script navigate to the directory and use the following command to created the necessary tables
    $ psql -f tournament.sql


    Running Test File
    ------------------    
    Included in the library is a python script to test the library with player senarios.The test script requires that the database be already setup (See Setting up Environment) in the environment prior to running.

    TO run the test file navigate to the dirctory that contains the tournament.py and tournament_test.py files. Wse the following command to run the test file:
    $ python tournment_test.py

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
