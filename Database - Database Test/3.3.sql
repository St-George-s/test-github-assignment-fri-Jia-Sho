UPDATE Timeslot
SET endTime = "19:30"
WHERE showID IN (
    SELECT ShowID
    FROM Show
    WHERE showname LIKE 'Star Cooks'
)
AND airDate = "2024-12-24";