-- List all records of second_table with a name value, ordered by descending score
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

