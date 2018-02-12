/*
Given the CITY and COUNTRY tables, query the names of all the continents 
(COUNTRY.Continent) and their respective average city populations (CITY.Population) 
rounded down to the nearest integer.
*/

SELECT C2.CONTINENT, FLOOR(AVG(C1.POPULATION)) FROM CITY C1, COUNTRY C2
WHERE C1.COUNTRYCODE=C2.CODE
GROUP BY C2.CONTINENT;