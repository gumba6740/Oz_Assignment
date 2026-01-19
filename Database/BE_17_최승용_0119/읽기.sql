-- 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요
SELECT name, salary FROM employees;



-- Frontend 직책을 가진 직원 중에서 
-- 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요
SELECT name, position, salary
FROM employees
WHERE position = 'Frontend'
AND salary <= 90000;


-- 모든 직원을 position 별로 그룹화하여
-- 각 직책의 평균 연봉을 계산하세요
SELECT position, AVG(salary)
FROM employees
GROUP BY position;