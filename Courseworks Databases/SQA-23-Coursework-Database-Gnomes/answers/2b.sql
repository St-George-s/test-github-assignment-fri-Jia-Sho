SELECT gnomeName, SUM(quantity) AS [Total Gnomes Sold]
FROM Gnome, GnomePurchase
WHERE Gnome.gnomeID=GnomePurchase.gnomeID 
AND Description Like "%solar%"
GROUP BY gnomeName
ORDER BY SUM(quantity) DESC;