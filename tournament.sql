-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

-- table of all players

CREATE TABLE IF NOT EXISTS players
(
pID serial primary key ,
name varchar(50) ,
wins int DEFAULT 0,
matches int DEFAULT 0


);

-- table of all matches 
CREATE TABLE  IF NOT EXISTS matches
(
matchID serial primary key,

winner int  REFERENCES players(pID) ON DELETE CASCADE,,
loser int   REFERENCES players(pID) ON DELETE CASCADE,
);
