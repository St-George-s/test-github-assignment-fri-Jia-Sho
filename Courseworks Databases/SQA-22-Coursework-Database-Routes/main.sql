-- #2b (working ans)
SELECT Planner.forename, Planner.surname, Planner.PlannerNo, count(walk.walkID) AS [Total Participants]
FROM Planner, Route, Walk
WHERE Planner.plannerNO = Route.PlannerNo
AND Route.routeID = Walk.routeID
GROUP BY Planner.PlannerNO
ORDER BY [Total Participants] DESC;


-- #2c 
SELECT Walker.WalkerNo, Walker.forename, walker.surname, walker.telNo
FROM Walker, Walk, Route
WHERE walker.walkerNo = walk.walkerNo
AND walk.routeID = route.routeID
AND route.routeID IN (
    SELECT routeID
    FROM route
    WHERE distance = (SELECT max(distance) FROM route)
)
GROUP BY walker.walkerNo
ORDER BY walker.walkerNo ASC;



-- #2d
SELECT Route.routeID, woodName, description
FROM Route
WHERE footwear LIKE '%shoes%';
