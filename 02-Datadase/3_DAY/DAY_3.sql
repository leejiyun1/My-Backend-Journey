-- 챌린지(Chapter14__20)과제 1번

-- CREATE TABLE employees(
-- 	id INT auto_increment PRIMARY KEY,
--     name VARCHAR(100),
--     position VARCHAR(100),
--     salary DECIMAL(10, 2)
-- )

-- 챌린지(Chapter14__20)과제 2번

-- INSERT INTO employees (name, position, salary)
-- VALUES 
-- ('혜린', 'PM', 90000),
-- ('은우', 'Frontend', 80000),
-- ('가을', 'Backend', 92000),
-- ('지수', 'Frontend', 78000),
-- ('민혁', 'Frontend', 96000),
-- ('하온', 'Backend', 130000);

-- 챌린지(Chapter14__20)과제 3번

-- SELECT name, salary FROM employees;


-- 챌린지(Chapter14__20)과제 4번

-- SELECT name, salary FROM employees
-- WHERE position = 'Frontend' AND salary<= 90000;


-- 챌린지(Chapter14__20)과제 5번

-- SET SQL_SAFE_UPDATES = 0; -- 세이프 모드 해제
-- UPDATE employees
-- SET salary = salary * 1.10
-- WHERE position = 'PM';
-- SELECT * FROM employees WHERE name = '혜린'; -- 인상 확인


-- 챌린지(Chapter14__20)과제 6번

-- UPDATE employees
-- SET salary = salary * 1.05
-- WHERE position = 'Backend';


-- 챌린지(Chapter14__20)과제 7번

-- DELETE FROM employees WHERE name = '민혁';


-- 챌린지(Chapter14__20)과제 8번

-- SELECT position, AVG(salary) AS average_salary
-- FROM employees
-- GROUP BY position;


-- 챌린지(Chapter14__20)과제 9번

-- DROP TABLE employees;


