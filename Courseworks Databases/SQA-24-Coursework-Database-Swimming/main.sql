-- SELECT Swimmer.initial, swimmer.surname, swimmer.swimCategory, team.teamName, COUNT(result.position) AS [Races won]
-- FROM Swimmer, team, Result
-- WHERE swimmer.teamRef = team.teamRef
-- AND result.swimmerID = swimmer.swimmerID
-- AND result.position = 1 
-- GROUP BY swimmer.swimmerID 
-- ORDER BY swimmer.initial ASC;



-- SELECT swimmer.initial, swimmer.surname, team.teamname, event.city, event.eventDate, result.lane
-- FROM swimmer, team, Event, result
-- WHERE swimmer.teamRef = team.teamRef
-- AND swimmer.swimmerID = result.swimmerID
-- AND result.raceTime = (
--     SELECT MIN(raceTime)
--     FROM result
--     WHERE (result.lane = 1 OR result.lane = 8)
-- )
-- GROUP BY swimmer.initial;


SELECT team.teamName, COUNT(result.position) AS [Total medals won]
FROM Result, Swimmer, Team
WHERE Result.swimmerID = Swimmer.swimmerID 
AND Swimmer.teamRef = Team.teamRef
AND (position = 1 OR position = 2 OR position = 3)
GROUP BY teamName
ORDER BY [Total medals won] DESC ;