CREATE TABLE IF NOT EXISTS user_shares (
  id INT PRIMARY KEY,
  user_id INT,
  symbol TEXT,
  shares INT,
  price FLOAT
);
CREATE TABLE IF NOT EXISTS transactions (
  id INT PRIMARY KEY,
  user_id INT,
  symbol TEXT,
  shares INT,
  price FLOAT,
  transacted TIMESTAMP
);
CREATE TABLE IF NOT EXISTS companies (symbol TEXT UNIQUE, name TEXT);
SELECT name FROM sqlite_master;