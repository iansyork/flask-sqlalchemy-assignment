DROP database if exists MovieRating;
Create DATABASE MovieRating;
use MovieRating;
-- Create movie table
DROP TABLE if EXISTS movie;

CREATE TABLE movie (
    movie_id SERIAL       NOT NULL,
    title    VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    rating   INT NOT      NULL,
    PRIMARY KEY (movie_id)
);
