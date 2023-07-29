# sys_sales_python_poo

## Stage 1  
Approach of solution:  
Python object-oriented without framework with memory storage  

Results:  

-- List of persons ---  
id:  1  | name:  Holger  | email:  holtech94@gmail.com  
id:  2  | name:  Luis  | email:  luis@gmail.com       
id:  3  | name:  Vasilisa  | email:  vasilisa@gmail.com  

 --- List of categories ---  
id: 1 | name: footwear  
id: 2 | name: clothes  
id: 3 | name: books  

--- List of products ---  
id: 1 | category: footwear | product: nike black shoes | description: footwear for men | unit-price: $ 30.0  
id: 2 | category: footwear | product: pink havaianas | description: footwear for women | unit-price: $ 9.5  
id: 3 | category: footwear | product: brown boots | description: footwear for men | unit-price: $ 55.0  
id: 4 | category: clothes | product: black jacket | description: clothes for men | unit-price: $ 110.0  
id: 4 | category: books | product: full stack django and react | description: packt pub book | unit-price: $ 39.0  
id: 5 | category: books | product: deep learning with tensorflow and keras | description: packt pub book | unit-price: $ 29.0    

--- List of products by category ---  

id-category: 1 | category: footwear  
----------------------------------------------  
Products:  
product-1: nike black shoes | unit-price: 30.0  
product-2: pink havaianas | unit-price: 9.5  
product-3: brown boots | unit-price: 55.0  

id-category: 2 | category: clothes  
----------------------------------------------  
Products:  
product-4: black jacket | unit-price: 110.0  

id-category: 3 | category: books  
----------------------------------------------  
Products:  
product-4: full stack django and react | unit-price: 39.0  
product-5: deep learning with tensorflow and keras | unit-price: 29.0  

--- List of suppliers ---  
id: 4 | name: Karina | num-orders: 0  
id: 5 | name: Fernando | num-orders: 0  

Register of orders for supplier: Karina:  
Status = supplier  
Number of orders = 2  
date: 2023-07-29 16:07:44.816735+00:00   ---  order-id = A001 ==> total = 429.0  
date: 2023-07-29 16:07:44.816735+00:00   ---  order-id = A003 ==> total = 47.5  

Register of orders for supplier: Fernando:  
Status = supplier  
Number of orders = 3  
date: 2023-07-29 16:07:44.816735+00:00   ---  order-id = A002 ==> total = 638.5  
date: 2023-07-29 16:07:44.816735+00:00   ---  order-id = A004 ==> total = 245.0  
date: 2023-07-29 16:07:44.816735+00:00   ---  order-id = A005 ==> total = 628.0  

--- List of suppliers ---
id: 4 | name: Karina | num-orders: 2  
id: 5 | name: Fernando | num-orders: 3  

--- List of Orders ---  
Order-id = A001    ----   date: 2023-07-29 16:07:44.816735+00:00  
Supplier: Karina  
    --- Order-detail ---  
Item 1 ==> Product: nike black shoes  | Unit-price: 30.0 | Qty: 10 |  Subtotal: 300.0  
Item 2 ==> Product: pink havaianas  | Unit-price: 9.5 | Qty: 2 |  Subtotal: 19.0  
Item 3 ==> Product: black jacket  | Unit-price: 110.0 | Qty: 1 |  Subtotal: 110.0  
Total for order A001: ------------------------- 429.0  

Order-id = A002    ----   date: 2023-07-29 16:07:44.816735+00:00  
Supplier: Fernando  
    --- Order-detail ---  
Item 1 ==> Product: nike black shoes  | Unit-price: 30.0 | Qty: 2 |  Subtotal: 60.0  
Item 2 ==> Product: pink havaianas  | Unit-price: 9.5 | Qty: 3 |  Subtotal: 28.5  
Item 3 ==> Product: brown boots  | Unit-price: 55.0 | Qty: 10 |  Subtotal: 550.0  
Total for order A002: ------------------------- 638.5  

Order-id = A003    ----   date: 2023-07-29 16:07:44.816735+00:00  
Supplier: Karina  
    --- Order-detail ---  
Item 1 ==> Product: pink havaianas  | Unit-price: 9.5 | Qty: 5 |  Subtotal: 47.5  
Total for order A003: ------------------------- 47.5  

Order-id = A004    ----   date: 2023-07-29 16:07:44.816735+00:00  
Supplier: Fernando  
    --- Order-detail ---  
Item 1 ==> Product: pink havaianas  | Unit-price: 9.5 | Qty: 2 |  Subtotal: 19.0  
Item 2 ==> Product: brown boots  | Unit-price: 55.0 | Qty: 2 |  Subtotal: 110.0  
Item 3 ==> Product: deep learning with tensorflow and keras  | Unit-price: 29.0 | Qty: 4 |  Subtotal: 116.0  
Total for order A004: ------------------------- 245.0  

Order-id = A005    ----   date: 2023-07-29 16:07:44.816735+00:00  
Supplier: Fernando  
    --- Order-detail ---  
Item 1 ==> Product: brown boots  | Unit-price: 55.0 | Qty: 10 |  Subtotal: 550.0  
Item 2 ==> Product: full stack django and react  | Unit-price: 39.0 | Qty: 2 |  Subtotal: 78.0  
Total for order A005: ------------------------- 628.0  
Accumulate of all orders: ----------------------------- 1988.0  


