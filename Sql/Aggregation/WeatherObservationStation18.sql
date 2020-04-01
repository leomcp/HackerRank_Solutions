/*
Consider P1(A,B) and P2(C,D) to be two points on a 2D plane.

 A,happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 B, happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 C, happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 D, happens to equal the maximum value in Western Longitude (LONG_W in STATION).
*/
SELECT 
  ROUND((ABS(MIN(LAT_N)-MAX(LAT_N))+ABS(MIN(LONG_W)-MAX(LONG_W))),4) FROM STATION;