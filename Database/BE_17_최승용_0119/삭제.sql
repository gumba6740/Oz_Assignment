SET SQL_SAFE_UPDATES = 0;

-- 민혁 사원의 데이터를 삭제하세요
DELETE FROM employees
WHERE name = '민혁';

SELECT * FROM employees;


-- employees 테이블을 삭제하세요
DELETE FROM employees;
DROP TABLE employees;


SET SQL_SAFE_UPDATES = 1;