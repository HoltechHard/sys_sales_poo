from typing import List
import datetime

# 1- class person
class Person:

    lst_persons: List["Person"] = []

    def __init__(self, id:int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        Person.lst_persons.append(self)
    
    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__}("
            f"{self.name}, {self.email}"
            f")"
        )

    def print_persons() -> None:
        print("--- List of persons ---")
        for person in Person.lst_persons:            
            print("id: ", person.id, " | name: ", person.name, " | email: ", person.email)

# 2- class supplier -> inherits Person
class Supplier(Person):

    lst_suppliers: List["Supplier"] = []

    def __init__(self, id: int, name: str, email: str) -> None:
        super().__init__(id, name, email)
        self.status = "supplier"
        self.orders: List["Order"] = []
        self.num_orders = 0
        Supplier.lst_suppliers.append(self)

    def insert_orders(self) -> None:
        # take all orders
        global_orders = Order.lst_orders

        # save just orders corresponding some specific supplier
        for u_order in global_orders:
            if u_order.supplier.id == self.id:
                self.orders.append(u_order)   
                self.num_orders += 1
    
    def print_suppliers() -> None:
        print("--- List of suppliers ---")
        for supplier in Supplier.lst_suppliers:
            print(f"id: {supplier.id} | name: {supplier.name} | num-orders: {supplier.num_orders}")

    def print_supplier_orders(self) -> None:
        # print the number of orders for supplier
        print(f"Register of orders for supplier: {self.name}: ")
        print(f"Status = {self.status}")
        print(f"Number of orders = {self.num_orders}")
        
        # print each order generated for supplier
        if self.orders:
            for order in self.orders:
                print(
                    f"date: {order.date_generated}   ---  "
                    f"order-id = {order.id} ==> total = {order.total}"
                )
        else:
            print(
                f"Supplier {self.name} doesnt made orders"
            )

# 3- class category
class Category:

    lst_categories: List["Category"] = []

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name 
        Category.lst_categories.append(self)
    
    def __repr__(self) -> None:
        return(
            f"{self.__class__.__name__}("
            f"{self.id}, {self.name}"
            f")"
        )

    def print_categories():
        print(" --- List of categories --- ")
        for category in Category.lst_categories:
            print(f"id: {category.id} | name: {category.name}")

# 4- class product
class Product:    

    lst_products: List["Product"] = []

    def __init__(self, id: int, category: Category,
                 name: str, description: str, unit_price: float) -> None:
        self.id = id
        self.category = category
        self.name = name
        self.description = description
        self.unit_price = unit_price
        Product.lst_products.append(self)

    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__}("
            f"{self.id}, {self.category.name}, "
            f"{self.name}, {self.description}, {self.unit_price}"
            f")"
        )
    
    def print_products() -> None:
        print("--- List of products ---")
        for product in Product.lst_products:
            print(
                f"id: {product.id} | category: {product.category.name} | "
                f"product: {product.name} | description: {product.description} | "
                f"unit-price: $ {product.unit_price}"
            )
    
    def print_category_products() -> None:
        print("--- List of products by category ---")
        for category in Category.lst_categories:
            print(f"id-category: {category.id} | category: {category.name}")
            print("----------------------------------------------")
            print("Products: ")
            for product in Product.lst_products:
                if product.category.id == category.id:
                    print(f"product-{product.id}: {product.name} | unit-price: {product.unit_price}")

# 5- class order detail 
# 1 order detail contain 1 product and quantity of products
class OrderDetail:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity
        self.subtotal = self.calculate_subtotal()

    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__}("
            f"{self.product}, {self.quantity}, {self.subtotal}"
            f")"
        )
    
    def calculate_subtotal(self) -> float:
        return self.product.unit_price * self.quantity

# 6- class order 
# 1 order contain 1 supplier and many details
class Order:

    lst_orders: List["Order"] = []
    accumulate_all_orders: float = 0.0

    def __init__(self, id: str, details: List["OrderDetail"], supplier: Supplier) -> None:
        self.id = id
        self.details = details
        self.supplier = supplier
        self.date_generated = datetime.datetime.now(tz = datetime.timezone.utc)
        self.total = 0.0
        Order.lst_orders.append(self)

    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__}("
            f"{self.id}, {self.details}, {self.supplier}, {self.total}"
            f")"
        )

    def calculate_total(self) -> float:
        for detail in self.details:
            self.total += detail.subtotal
        # sum to accumulate of all orders            
        Order.accumulate_all_orders += self.total
        
        return self.total
    
    def print_orders() -> None:
        print("--- List of Orders ---")
        for order in Order.lst_orders:
            print(f"Order-id = {order.id}    ----   date: {order.date_generated}")
            print(f"Supplier: {order.supplier.name}")
            print(f"    --- Order-detail ---")
            i = 0   
            for item in order.details:
                i += 1
                print(f"Item {i} ==> Product: {item.product.name}  | "
                      f"Unit-price: {item.product.unit_price} | Qty: {item.quantity} | "
                       f" Subtotal: {item.subtotal}")
            print(f"Total for order {order.id}: ------------------------- {order.total}")
        print(f"Accumulate of all orders: ----------------------------- {Order.accumulate_all_orders}")

