<<<<<<< HEAD
SELECT E.eventName, S.name AS [Shop Name] , E.maxAttendees , e.eventDate
FROM Event E, Shop S
WHERE E.shopID = S.shopID
GROUP BY E.eventName;



SELECT S.name AS [Shop Name], E.eventName
FROM Event E, Shop S
WHERE E.shopID = S.shopID
AND eventdate LIKE "2024-12-25"
GROUP BY e.eventName;




UPDATE OpeningTime
SET closeTime = "19:00"
WHERE shopID IN (
    SELECT shopID 
    FROM shop
    WHERE shop.name LIKE "Zara"
)
AND date LIKE "2024-12-24";

=======
>>>>>>> a8ee91c (Added Class Test)
