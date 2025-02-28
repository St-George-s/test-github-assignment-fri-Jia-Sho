-- 2c
SELECT Comic.comicTitle, Comic.issue, Publisher.publisherName, Comic.valuation
FROM Comic, Publisher
WHERE Comic.publisherID = Publisher.publisherID
AND Comic.valuation  > 300 + (SELECT AVG(valuation) FROM Comic);


-- 2d
SELECT CharacterInfo.characterName, SUM(Comic.valuation) AS [Total Valuation]
FROM CharacterInfo, Comic, ComicCharacter
WHERE ComicCharacter.characterID = CharacterInfo.characterID
AND ComicCharacter.comicID = Comic.comicID
AND CharacterInfo.characterName LIKE '%Duck%'
AND ComicCharacter.mainCharacter = 1
GROUP BY CharacterInfo.characterName
ORDER BY [Total Valuation] DESC;


-- 2e
SELECT Comic.comicTitle, Comic.issue, Publisher.publisherName, (Comic.valuation * 2) AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND CharacterInfo.characterName = "Starlordly"
AND Comic.publisherID = Publisher.publisherID
AND Comic.seriesID = Series.seriesID
AND CharacterInfo.characterID = ComicCharacter.characterID
AND Comic.comicID = ComicCharacter.comicID;


