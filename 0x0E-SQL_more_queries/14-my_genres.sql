-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT tv_genres.name
FROM hbtn_0d_tvshows.tv_genres
JOIN hbtn_0d_tvshows.tv_show_genres ON hbtn_0d_tvshows.tv_genres.id = hbtn_0d_tvshows.tv_show_genres.genre_id
JOIN hbtn_0d_tvshows.tv_shows ON hbtn_0d_tvshows.tv_show_genres.show_id = hbtn_0d_tvshows.tv_shows.id
WHERE hbtn_0d_tvshows.tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

