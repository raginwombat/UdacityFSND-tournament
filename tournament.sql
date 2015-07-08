-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.




create table players(
id  serial Primary Key,
name varchar(55));

create table matches(
#match_id serial,
round   serial,
winner integer  References players(id),
loser integer References players(id) );


create table player_records(
id integer  References players(id), 
wins integer,
losses integer);
