-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT tv_shows.title, tv_genres.name
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON hbtn_0d_tvshows.tv_shows.id = hbtn_0d_tvshows.tv_show_genres.show_id
LEFT JOIN hbtn_0d_tvshows.tv_genres ON hbtn_0d_tvshows.tv_show_genres.genre_id = hbtn_0d_tvshows.tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

