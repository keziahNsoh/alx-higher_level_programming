-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered by descending show title.
SELECT tv_shows.title
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON hbtn_0d_tvshows.tv_shows.id = hbtn_0d_tvshows.tv_show_genres.show_id
JOIN hbtn_0d_tvshows.tv_genres ON hbtn_0d_tvshows.tv_show_genres.genre_id = hbtn_0d_tvshows.tv_genres.id
WHERE hbtn_0d_tvshows.tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

