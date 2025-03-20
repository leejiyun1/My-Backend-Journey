-- 하나하나 입력하기 보단 개념을 이해했다는 의미로 작성했습니다.
-- 생성 과제
-- - 초급

--     (1) **`customers`** 테이블에 새 고객을 추가하세요.
    INSERT INTO customers (customerName, phone, addressLine1 ....)
    VALUES ('ozcoding', 01094478446,......);

--     (2) **`products`** 테이블에 새 제품을 추가하세요.
    INSERT INTO products (productsCode, productsName, productLine...)
    VALUES (123, '비싼거','비싼공장');
    
--     (3) **`employees`** 테이블에 새 직원을 추가하세요.
    INSERT INTO employees (name, )
    VALUES ('이지윤');
    
--     (4) **`offices`** 테이블에 새 사무실을 추가하세요.
    INSERT INTO offices (...)
    VALUES (...)
    
--     (5) **`orders`** 테이블에 새 주문을 추가하세요.
    INSERT INTO orders (...)
    VALUES (...)
    
--     (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
    INSERT INTO orderdetails (...)
    VALUES (...)
    
--     (7) **`payments`** 테이블에 지불 정보를 추가하세요.
    INSERT INTO payments (...)
    VALUES (...)
    
--     (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
    INSERT INTO productlines (...)
    VALUES (...)
    
--     (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
    INSERT INTO customers (customerName, phone, addressLine1 ....)
    VALUES ('ozcoding', 01094478446, '다른 지역');
    
--     (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
    INSERT INTO products (...)
    VALUES (...)


-- - 중급
    
--     (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.
    INSERT INTO customers (customerName, phone, addressLine1 ....)
    VALUES ('ozcoding1', 01094478446,......),
            ('ozcoding2', 01094478447,......),
            ('ozcoding3', 01094478448,......),
            ('ozcoding4', 01094478449,......),
            ('ozcoding5', 01094478440,......);


--     (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.
    
--     (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.
    
--     (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.
    INSERT INTO orders (order_id ...) VALUES (1, ...)
    INSERT INTO orderdetails (order_id ...) VALUES (1, ...);
    
--     (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.
    
--     (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.
    
--     (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.
    
--     (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.
    
--     (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.
    
--     (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.
    INSERT INTO productlines (productLine, ...) VALUES ('aaa'....)
    INSERT INTO products (productLine, ....)
    VALUES ('aaa',....),
            ('aaa',....),
            ('aaa',....),
            ('aaa',....),
            ('aaa',....);


-- - 고급
    
--     (1) **`customers`** 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.
    INSERT INTO customers (customerNumber, ...) VALUES (1, ...)
    INSERT INSERT orders (customerNumber, ... ) VALUES (1, ...);
    
--     (2) **`employees`** 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이트하세요.
    
--     (3) **`products`** 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.
    
--     (4) **`orders`** 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.
    
--     (5)**`orderdetails`** 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.
    INSERT INTO orderdetails (productCode, quantityOrdered ,...) VALUES ( '1', 2, ...)
    UPDATE products
    SET quantityInStock = quantityInStock - 2
    WHERE productCode = '1';

-- 읽기 과제
-- - 초급
    
--     (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
    SELECT * FROM customers;
    
--     (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
    SELECT * FROM products;
    
--     (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
    SELECT fristName ,lastName, jobTitle FROM employees;
    
--     (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
    SELECT officeCode, city, country FROM offices;
    
--     (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
    SELECT * FROM orders
    ORDER BY orderDate DESC
    LIMIT 10;
    
--     (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
    SELECT * FROM orderdetails
    WHERE orderNumber = 1;
    
--     (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
    SELECT * FROM payments
    WHERE customerNumber = 1;
    
--     (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
    
--     (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
    
--     (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
    SELECT * FROM products
    WHERE buyPrice BETWEEN 100 AND 200;

-- - 중급
    
--     (1) **`orders`** 테이블에서 특정 고객의 모든 주문을 조회하세요.
    
--     (2) **`orderdetails`** 테이블에서 특정 제품에 대한 모든 주문 상세 정보를 조회하세요.
    
--     (3) **`payments`** 테이블에서 특정 기간 동안의 모든 지불 정보를 조회하세요.
    
--     (4) **`employees`** 테이블에서 특정 직급의 모든 직원을 조회하세요.
    
--     (5) **`offices`** 테이블에서 특정 국가의 모든 사무실을 조회하세요.
    
--     (6) **`productlines`** 테이블에서 특정 제품 라인에 속하는 모든 제품을 조회하세요.
    
--     (7) **`customers`** 테이블에서 최근에 가입한 5명의 고객을 조회하세요.
    
--     (8) **`products`** 테이블에서 재고가 부족한 모든 제품을 조회하세요.
    
--     (9) **`orders`** 테이블에서 지난 달에 이루어진 모든 주문을 조회하세요.
    
--     (10) **`orderdetails`** 테이블에서 특정 주문에 대한 총 금액을 계산하세요.

-- - 고급
    
--     (1) **`customers`** 테이블에서 각 지역별 고객 수를 계산하세요.
    
--     (2) **`products`** 테이블에서 각 제품 카테고리별 평균 가격을 계산하세요.
    
--     (3) **`employees`** 테이블에서 각 부서별 직원 수를 계산하세요.
    
--     (4) **`offices`** 테이블에서 각 사무실별 평균 직원 연봉을 계산하세요.
    
--     (5) **`orderdetails`** 테이블에서 가장 많이 팔린 제품 5개를 조회하세요.

-- 갱신 과제
    -- - 초급
        
    --     (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
    UPDATE customers SET addressLine1 = '우리집은 어딘가'
    WHERE customerNumber = 1;
        
    --     (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
    UPDATE products SET buyPrice = 2472398758
    WHERE productCode = '1';
        
    --     (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
        
    --     (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
        
    --     (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
        
    --     (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
        
    --     (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
        
    --     (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
        
    --     (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
        
    --     (10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
    UPDATE products
    SET buyPrice = CASE
        WHEN productCode = '1' THEN 5000
        WHEN productCode = '2' THEN 6000
        WHEN productCode = '3' THEN 7000
    END
    WHERE productCode IN ('1','2','3')

-- 중급 10문제
-- 고급 5문제

-- 삭제 과제
-- - 초급
    
--     (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
    DELETE FROM customers
    WHERE customerNumber = 1;
    
--     (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
    DELETE FROM products
    WHERE productCode = '1';
    
--     (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
    
--     (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
    
--     (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
    
--     (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
    
--     (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
    
--     (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
    
--     (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
    DELETE FROM customers
    WHERE city = '이지윤시';
    
--     (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.

-- 중급 10문제
-- 고급 5문제

