SELECT artist_name 
FROM Artists 
WHERE artist_name LIKE 'T%';


SELECT album_name, release_year 
FROM Albums 
WHERE release_year >= 2015 
ORDER BY release_year DESC;


SELECT a.album_name AS Album, a.release_year Year 
FROM Albums a 
WHERE a.release_year > 2010 
ORDER BY a.release_year;


SELECT artist_name, LENGTH(artist_name) AS Name_Length 
FROM Artists 
WHERE artist_name LIKE '_a%';

SELECT track_name
FROM Tracks
WHERE track_name LIKE 's%e';

SELECT album_name, 
       release_year, 
       2024 - release_year AS years_ago
FROM albums
WHERE release_year > 2010
ORDER BY release_year DESC;

SELECT artist_name, LENGTH(artist_name) AS Name_Length
FROM Artists
WHERE Name_Length > 5;