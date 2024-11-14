-- SELECT COUNT(*)
-- FROM Tracks
-- WHERE duration_ms>266000;

SELECT genre_id, COUNT(*)
FROM Tracks 
GROUP BY genre_id;


-- SELECT genre_id, AVG(duration_ms)
-- FROM Tracks 
-- GROUP BY genre_id;