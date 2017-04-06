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
name varchar(50) 



);

-- table of all matches 
CREATE TABLE  IF NOT EXISTS matches
(
matchID serial primary key,

winner int  REFERENCES players(pID) ON DELETE CASCADE,
loser int   REFERENCES players(pID) ON DELETE CASCADE
);

-- Standing views
CREATE OR REPLACE VIEW standings AS
SELECT players.pID, players.name,
	SUM( CASE WHEN matches.winner = players.pID THEN 1 ELSE 0 END ) AS wins,
	count(matches.*) AS matches
FROM players LEFT JOIN matches
ON players.pID = matches.winner OR players.pID = matches.loser
GROUP BY players.pID;