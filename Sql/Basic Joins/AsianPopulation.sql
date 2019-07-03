/*
Given the CITY and COUNTRY tables, query the sum of the populations of all 
cities where the CONTINENT is 'Asia'.
*/
SELECT SUM(C1.POPULATION) FROM CITY C1, COUNTRY C2
WHERE 
C1.COUNTRYCODE =C2.CODE 
AND 
C2.CONTINENT='Asia';