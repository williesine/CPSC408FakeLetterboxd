CREATE TABLE actors(
    actorID INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(40),
    avgRating INTEGER
);

CREATE TABLE directors(
    directorID INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(40),
    avgRating INTEGER
);

CREATE TABLE movies(
    movieID VARCHAR(20) PRIMARY KEY NOT NULL,
    directorID INTEGER,
    title VARCHAR(120),
    description VARCHAR(1000),
    genre VARCHAR(20),
    runTime INTEGER, -- MINUTES
    releaseYear INTEGER,
    imdbScore DECIMAL(2, 1),
    FOREIGN KEY (directorID) REFERENCES directors(directorID)
);

-- table for M-M relationship from movies to actors
CREATE TABLE movieActors(
    movieID VARCHAR(20) NOT NULL,
    actorID INTEGER NOT NULL,
    PRIMARY KEY (movieID, actorID)
);
-- table for M-M relationship from tvShows to actors
CREATE TABLE tvShowActors(
    tvShowID VARCHAR(20) NOT NULL,
    actorID INTEGER NOT NULL,
    PRIMARY KEY (tvShowID, actorID)
);

CREATE TABLE tvShows(
    tvShowID VARCHAR(20) PRIMARY KEY NOT NULL,
    directorID INTEGER,
    title VARCHAR(120),
    genre VARCHAR(15),
    runTime INTEGER, -- MINUTES
    releaseYear INTEGER,
    seasons INTEGER,
    imdbScore DECIMAL(2, 1),
    FOREIGN KEY (directorID) REFERENCES directors(directorID)
);

CREATE TABLE reviews(
    reviewID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    writtenReviews VARCHAR(256),
    tvShowID VARCHAR(20),
    movieID VARCHAR(20),
    userID INTEGER,
    userRating INTEGER,
    FOREIGN KEY (tvShowID) REFERENCES tvShows(tvShowID),
    FOREIGN KEY (movieID) REFERENCES movies(movieID),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE users(
    userID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(20)
);

CREATE TABLE titlesWhole(
    id VARCHAR(20),
    title VARCHAR(120),
    type VARCHAR(10),
    description VARCHAR(1500),
    release_year INTEGER,
    age_certification VARCHAR(10),
    runtime INTEGER,
    genre VARCHAR(30),
    production_country VARCHAR(5),
    seasons INTEGER,
    imdb_id VARCHAR(20),
    imdb_score DECIMAL(2, 1),
    imdb_votes INTEGER
);

CREATE TABLE creditsWhole(
    person_id INTEGER,
    id VARCHAR(20),
    name VARCHAR(40),
    character_name VARCHAR(500),
    role VARCHAR(10)
);