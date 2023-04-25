-- insert into actors table
INSERT INTO actors (actorID, name)
    SELECT DISTINCT person_id, name
    FROM creditsWhole
    WHERE role = 'ACTOR';

-- insert into directors table
INSERT INTO directors (directorID, name)
    SELECT DISTINCT person_id, name
    FROM creditsWhole
    WHERE ROLE = 'DIRECTOR';

-- populate movies table (without directorID)
INSERT INTO movies (movieID, title, description, genre, runTime, releaseYear, imdbScore)
    SELECT id, title, description, genre, runtime, release_year, imdb_score
    FROM titlesWhole
    WHERE type = 'MOVIE';

-- populate tvShows table (without directorID)
INSERT INTO tvShows (tvShowID, title, genre, runTime, releaseYear, seasons, imdbScore)
    SELECT id, title, genre, runtime, release_year, seasons, imdb_score
    FROM titlesWhole
    WHERE type = 'SHOW';

INSERT INTO movieActors
    SELECT DISTINCT creditsWhole.id, creditsWhole.person_id
    FROM creditsWhole INNER JOIN movies ON creditsWhole.id = movies.movieID
    WHERE creditsWhole.role = 'ACTOR';

INSERT INTO tvShowActors
    SELECT DISTINCT creditsWhole.id, creditsWhole.person_id
    FROM creditsWhole INNER JOIN tvShows ON creditsWhole.id = tvShows.tvShowID
    WHERE creditsWhole.role = 'ACTOR';

-- fills in the directorID column with the matched movies
UPDATE movies m
SET directorID = (
    SELECT person_id
    FROM creditsWhole cW
    WHERE m.movieID = cW.id
    AND role = 'DIRECTOR'
    LIMIT 1
    );

-- fills in the directorID column with the matched tvShows
UPDATE tvShows tv
SET directorID = (
    SELECT person_id
    FROM creditsWhole cW
    WHERE tv.tvShowID = cW.id
    AND role = 'DIRECTOR'
    LIMIT 1
    );
