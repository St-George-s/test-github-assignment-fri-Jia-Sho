

-- SELECT Comic.comicTitle, Comic.issue, Publisher.publisherName, Comic.valuation
-- FROM Comic, Publisher
-- WHERE Comic.publisherID = Publisher.publisherID
-- AND Comic.valuation  IN (
--     SELECT AVG(valuation)
--     FROM Comic;
-- );

-- SELECT AVG(valuation)
-- FROM Comic;




-- SELECT CharacterInfo.characterName, SUM(Comic.valuation) AS [Total Valuation]
-- FROM CharacterInfo, Comic, ComicCharacter
-- WHERE ComicCharacter.characterID = CharacterInfo.characterID
-- AND ComicCharacter.comicID = Comic.comicID
-- AND CharacterInfo.characterName LIKE '%Duck%'
-- GROUP BY CharacterInfo.characterName;



-- ComicCharacter.mainCharacter




SELECT CharacterInfo.characterName, SUM(Comic.valuation) AS [Total Valuation]
FROM CharacterInfo, Comic, ComicCharacter
WHERE ComicCharacter.mainCharacter LIKE '%Duck%'
AND ComicCharacter.characterID = CharacterInfo.characterID
AND ComicCharacter.comicID = Comic.comicID
GROUP BY CharacterInfo.characterName;




