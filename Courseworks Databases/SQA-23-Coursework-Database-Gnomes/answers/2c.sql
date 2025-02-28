
SELECT C.emailAddress, P.orderID, P.quantity
FROM Customer C, GnomePurchase P , Orders O  
WHERE P.orderID = O.orderID AND
      O.customerID = C.customerID AND
      P.quantity >= 3 AND
      P.GnomeID IN (
    SELECT GnomeID 
    FROM Gnome 
    WHERE unitprice = (select MAX(unitprice) from Gnome)
);
