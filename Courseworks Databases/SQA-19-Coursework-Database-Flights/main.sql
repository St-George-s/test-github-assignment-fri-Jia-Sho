SELECT Customer.forename, customer.surname, SUM(booking.adultTicket * 5.50 + booking.childTicket * 2.00 + booking.concessionTicket * 1.50) AS [Tax (£)]
FROM customer, booking
WHERE customer.customerID = booking.customerID
AND booking.customerID = 'GR01932'
AND booking.flightID = 'QH182';


SELECT customer.forename , customer.surname
FROM customer, booking
WHERE customer.customerID = booking.customerID
AND childTicket IN (
    SELECT MAX(childTicket)
    FROM Booking
);