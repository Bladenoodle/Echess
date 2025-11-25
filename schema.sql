CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE matches (
    id INTEGER PRIMARY KEY,
    player_id1 INTEGER REFERENCES users,
    player_id2 INTEGER REFERENCES users,
);

CREATE TABLE boards (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

