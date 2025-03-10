# dragon-ball-z


--https://www.w3schools.com/sql/default.asp
--QUERY 1
SELECT *
FROM Track
WHERE UnitPrice <= "0.99";
--QUERY 2
SELECT *
FROM Artist
WHERE Name like "%a%";
--QUERY 3
SELECT *
FROM Invoice
WHERE BillingCountry = "Canada";
--QUERY 4
SELECT COUNT(TrackId) 
AS Tracks FROM Track;
--QUERY 5
SELECT Album.Title, Artist.Name
FROM Album
JOIN Artist ON Album.ArtistId = Artist.ArtistId;
--QUERY 6
SELECT *
FROM Track
WHERE UnitPrice BETWEEN 0.99 AND 1.99
ORDER BY UnitPrice DESC
LIMIT 5;
--QUERY 7
SELECT BillingCountry, SUM(Total) AS "TotalSales"
FROM Invoice
GROUP BY BillingCountry
ORDER BY TotalSales DESC;
--QUERY 8
SELECT CustomerId, COUNT(*) AS InvoiceCount
FROM Invoice
GROUP BY CustomerId;
--QUERY 9
SELECT a.Title, COUNT(t.TrackId) AS TrackCount
FROM Album a
JOIN Track t ON a.AlbumId = t.AlbumId
GROUP BY a.AlbumId
HAVING TrackCount > 10;




--QUERY 10
SELECT *
FROM Invoice
WHERE BillingCity LIKE "%york%";
--QUERY 11
SELECT Artist.Name, COUNT(Album.AlbumId) AS AlbumCount
FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId
GROUP BY Artist.Name
ORDER BY AlbumCount DESC
LIMIT 1;
--QUERY 12
SELECT CustomerId, SUM(Total) AS TotalSpent
FROM Invoice
GROUP BY CustomerId
ORDER BY TotalSpent DESC
LIMIT 3;
--QUERY 13
SELECT EmployeeId, FirstName, LastName  
FROM Employee  
WHERE ReportsTo = "1";
--QUERY 14
SELECT Genre.Name, COUNT(Track.TrackId) AS TrackCount
FROM Genre JOIN Track ON Genre.GenreId = Track.GenreId
GROUP BY Genre.Name
ORDER BY TrackCount DESC
LIMIT 1;
--QUERY 15
SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS TotalSpent
FROM Customer 
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
HAVING TotalSpent > 30
ORDER BY TotalSpent DESC;

