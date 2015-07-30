-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Create Player Table, stores player names and auto generates the palyer ID

CREATE TABLE players(
id  SERIAL PRIMARY KEY,
name varchar(55));

--Creates the match storage, round is auto generated, winner and loser ID are recorded
CREATE TABLE matches(
round   SERIAL,
winner INTEGER  REFERENCES players(id),
loser INTEGER REFERENCES players(id) );


CREATE TABLE player_records(
id INTEGER  REFERENCES players(id), 
wins INTEGER DEFAULT 0,
losses INTEGER DEFAULT 0);

--View used to simplify code, returns an orderd set of Swiss Pairings
CREATE VIEW swissQuery AS
SELECT players.id, players.name
FROM players
JOIN player_records 
	ON players.id = player_records.id
ORDER BY player_records.wins DESC;


CREATE VIEW standingsQuery AS
SELECT players.id,name, player_records.wins, (player_records.wins + player_records.losses) 
AS matches
FROM (
	players 
	FULL JOIN player_records 
	ON players.id = player_records.id);