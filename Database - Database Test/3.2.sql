SELECT show.showName AS [Show] , Episode.episodeTitle AS [Episode]
FROM show, episode
WHERE episodeDate LIKE '2024-12-__'
AND show.showID = episode.showID;