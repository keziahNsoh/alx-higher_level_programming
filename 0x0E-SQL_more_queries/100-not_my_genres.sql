-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM hbtn_0d_tvshows.tv_genres
WHERE hbtn_0d_tvshows.tv_genres.id NOT IN (
    SELECT DISTINCT hbtn_0d_tvshows.tv_show_genres.genre_id
    FROM hbtn_0d_tvshows.tv_show_genres
    JOIN hbtn_0d_tvshows.tv_shows ON hbtn_0d_tvshows.tv_show_genres.show_id = hbtn_0d_tvshows.tv_shows.id
    WHERE hbtn_0d_tvshows.tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
