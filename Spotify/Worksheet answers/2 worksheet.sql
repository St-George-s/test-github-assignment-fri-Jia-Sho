DELETE FROM Tracks 
WHERE track_id = 5;

SELECT *
FROM Tracks


DELETE FROM Artists 
WHERE artist_id BETWEEN 20 AND 25;

SELECT *
FROM Artists


INSERT INTO Genres (genre_id, genre_name) 
VALUES (21, 'Jazz');

SELECT *
FROM Genres


INSERT INTO Tracks (track_id, track_name, artist_id, album_id, genre_id, duration_ms) 
VALUES (54, 'New Track', 4, 4, 1, 180000), 
       (55, 'Another Track', 5, 5, 2, 200000);

SELECT *
FROM Tracks


UPDATE Albums 
SET release_year = 2021 
WHERE album_id = 3;

SELECT *
FROM Albums


UPDATE Artists 
SET artist_name = 'New Artist Name' 
WHERE artist_id IN (1, 2, 3);

SELECT *
FROM Artists
