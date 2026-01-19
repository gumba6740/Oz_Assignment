SET SQL_SAFE_UPDATES = 0;


-- PM직책을 가진 직원의 연봉을 10% 인상한 후 결과를 확인
UPDATE employees
SET salary = salary * 1.10
WHERE position = 'PM';

SELECT * FROM employees;


-- 모든 Backend 직원의 연봉을 5% 인상
UPDATE employees
SET salary = salary * 1.05
WHERE position = 'Backend';


SET SQL_SAFE_UPDATES = 1;