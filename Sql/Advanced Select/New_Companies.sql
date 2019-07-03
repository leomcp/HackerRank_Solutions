/*
Enter your query here.
*/

select company_code, founder, 
(Select count(distinct lead_manager_code) from Lead_Manager where company_code = C.company_code ), 
(select count(distinct senior_manager_code) from Senior_Manager where company_code = C.company_code), 
(select count(distinct manager_code) from Manager where company_code = C.company_code), 
(select count(distinct employee_code) from Employee where company_code = C.company_code )
from Company C
order by company_code 