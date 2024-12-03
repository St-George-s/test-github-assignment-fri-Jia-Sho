SELECT p.forename, p.surname, p.plannerNo , count(*) AS [Total Participants]
FROM Planner P, Route R, Walk W, Walker WR
WHERE p.plannerNo = r.plannerNo
AND r.routeID = W.routeID
AND w.walkerno = WR.walkerno;