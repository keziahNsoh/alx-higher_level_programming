-- List all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_rates ON tv_show_genres.show_id = tv_show_rates.show_id
GROUP BY tv_genres.id
ORDER BY rating_sum DESC;

