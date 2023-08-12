# sys_sales_python_poo
Small system for orders control using python-OO from scratch    

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


## Stage 2  
Approach of solution:  
Python object-oriented without framework with mysql database storage  

### Database model:  
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/cc553fb6-e5ac-4d8f-a246-536251437d4a)  

### Database components:  
Tables: 9  
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/aa2859d0-684f-41c3-b227-15027a9789fa)  
Views: 9  
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/f518fed3-d606-496c-92ee-0990b9d277de)  
Store procedures: 18 and Cursor: 1  
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/e479aaa3-8483-4a85-9bef-da4788fe5a55)  
Triggers: 3  
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/6e8aad4f-7aae-42ee-b572-61e57ddad303)  

### Results:  
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/7b7e0f36-e45e-43fc-939c-c449301b9e25) 
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/391a2aef-9b6d-498e-9fda-bbe7fa19e6d9)
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/774655a1-a458-4dd7-aa6d-c12b3d19e6b8)
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/391c79b1-3724-4f5c-8f3c-5b0ed399459c)
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/fe3ac579-5c44-4cfb-8551-782e7e9feb3c)
![image](https://github.com/HoltechHard/sys_sales_poo/assets/35493202/24e61f8b-ba45-4feb-a5e0-6a6844284496)

