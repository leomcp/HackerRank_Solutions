/*
Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
*/
SELECT C1.NAME FROM CITY C1, COUNTRY C2 
WHERE C2.CONTINENT='Africa'
AND 
C1.COUNTRYCODE=C2.CODE;