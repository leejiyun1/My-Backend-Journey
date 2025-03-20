-- 하나하나 입력하기 보단 개념을 이해했다는 의미로 작성했습니다.
-- 생성 과제
-- - 초급

--     (1) **`customers`** 테이블에 새 고객을 추가하세요.
    INSERT INTO customers (customerName, phone, addressLine1 ....)
    VALUES ('ozcoding', 01094478446,......)

--     (2) **`products`** 테이블에 새 제품을 추가하세요.
    INSERT INTO products (productsCode, productsName, productLine...)
    VALUES (123, '비싼거','비싼공장')
    
--     (3) **`employees`** 테이블에 새 직원을 추가하세요.
    INSERT INTO employees (name, )
    VALUES ('이지윤')
    
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
    VALUES ('ozcoding', 01094478446, '다른 지역')
    
--     (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
    INSERT INTO products (...)
    VALUES (...)


-- - 중급
    
--     (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.
    INSERT INTO customers (customerName, phone, addressLine1 ....)
    VALUES ('ozcoding1', 01094478446,......)
            ('ozcoding2', 01094478447,......)
            ('ozcoding3', 01094478448,......)
            ('ozcoding4', 01094478449,......)
            ('ozcoding5', 01094478440,......)


--     (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.
    
--     (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.
    
--     (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.
    INSERT INTO orders (order_id ...) VALUES (1, ...)
    INSERT INTO orderdetails (order_id ...) VALUES (1, ...)
    
--     (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.
    
--     (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.
    
--     (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.
    
--     (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.
    
--     (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.
    
--     (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.
    INSERT INTO productlines (productLine, ...) VALUES ('aaa'....)
    INSERT INTO products (productLine, ....)
    VALUES ('aaa',....)
            ('aaa',....)
            ('aaa',....)
            ('aaa',....)
            ('aaa',....)


-- - 고급
    
--     (1) **`customers`** 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.
    INSERT INTO customers (customerNumber, ...) VALUES (1, ...)
    INSERT INSERT orders (customerNumber, ... ) VALUES (1, ...)
    
--     (2) **`employees`** 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이트하세요.
    
--     (3) **`products`** 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.
    
--     (4) **`orders`** 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.
    
--     (5)**`orderdetails`** 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.
    INSERT INTO orderdetails (productCode, quantityOrdered ,...) VALUES ( '1', 2, ...)
    UPDATE products
    SET quantityInStock = quantityInStock - 2
    WHERE productCode = '1'

-- 읽기 과제
-- 초급 10문제
-- 중급 10문제
-- 고급 5문제

-- 갱신 과제
-- 초급 10문제
-- 중급 10문제
-- 고급 5문제

-- 삭제 과제
-- 초급 10문제
-- 중급 10문제
-- 고급 5문제

