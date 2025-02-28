SELECT Episode.episodeTitle, Show.showName, Episode.MaxViewers,Episode.episodeDate
FROM Episode, Show
WHERE Show.showID = Episode.showID;