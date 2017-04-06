# Tournament-Results


This is You will develop a database schema to store the game matches between players. You will then write code to query this data and determine the winners of various games in a Swiss style tournament .

Understand the purpose of each file:
  - `tournament.sql`  this file is used to set up the database schema
  - `tournament.py`  this file is used to provide access to the database via a library of functions which can add, delete or query data in your database to another python program 
  - `tournament_test.py` contains a number of test functions
  

# How to run

1. Initialize the database using `psql`
  `\i tournament.sql`
2. Quit `psql`
3. Run `python tournament_test.py`
  
