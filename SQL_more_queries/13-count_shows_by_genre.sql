-- Script that lists all genres and displays the number of shows linked to each.
SELECT tv_shows.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;