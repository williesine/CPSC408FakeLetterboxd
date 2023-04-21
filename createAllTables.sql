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
    movieID INTEGER PRIMARY KEY NOT NULL,
    directorID INTEGER,
    title VARCHAR(120),
    description VARCHAR(1000),
    genre VARCHAR(20),
    runTime INTEGER, -- MINUTES
    releaseYear INTEGER
    FOREIGN KEY (directorID) REFERENCES directors(directorID)
);

-- table for M-M relationship from movies to actors
CREATE TABLE movieActors(
    movieID INTEGER PRIMARY KEY NOT NULL,
    actorID INTEGER PRIMARY KEY NOT NULL
);
-- table for M-M relationship from tvShows to actors
CREATE TABLE tvShowActors(
    tvShowID INTEGER PRIMARY KEY NOT NULL,
    actorID INTEGER PRIMARY KEY NOT NULL
);

CREATE TABLE tvShows(
    tvShowID INTEGER PRIMARY KEY NOT NULL,
    directorID INTEGER,
    title VARCHAR(120),
    imdbScore INTEGER,
    genre VARCHAR(15),
    runTime INTEGER, -- MINUTES
    releaseYear INTEGER,
    seasons INTEGER,
    FOREIGN KEY (directorID) REFERENCES directors(directorID)
);

CREATE TABLE reviews(
    reviewID INTEGER PRIMARY KEY NOT NULL,
    writtenReviews VARCHAR(256),
    tvShowID INTEGER
    movieID INTEGER,
    userID INTEGER,
    userRating INTEGER
    FOREIGN KEY (tvShowID) REFERENCES tvShows(tvShowID)
    FOREIGN KEY (movieID) REFERENCES movies(movieID)
    FOREIGN KEY (userID) REFERENCES users(userID)

);

CREATE TABLE users(
    userID INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(20)
);