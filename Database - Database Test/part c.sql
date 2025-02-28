SELECT show.showName, count(Viewerrating.ratingValue) AS [TotalRatings] 
FROM show, Viewerrating, episode
WHERE show.showID = episode.showID
AND episode.episodeID = Viewerrating.episodeID
GROUP BY show.showname
ORDER BY count(Viewerrating.ratingValue) DESC ;

