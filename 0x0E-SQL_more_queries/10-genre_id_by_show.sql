--Select Genre ID by show

/*
 * This query lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
 * Each record displays the title of the show along with the corresponding genre ID.
 * Results are sorted in ascending order by show title and genre ID.
 */

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

