from models import Person, Category, Product, Supplier, Order, OrderDetail

def generate_person():
    # create the objects
    p1 = Person(1, "Holger", "holtech94@gmail.com")
    p2 = Person(2, "Luis", "luis@gmail.com")
    p3 = Person(3, "Vasilisa", "vasilisa@gmail.com")

    # print the list of contacts
    Person.print_persons()

def generate_category():
    # create the objects
    c1 = Category(1, "footwear")
    c2 = Category(2, "clothes")
    c3 = Category(3, "books")

    # print the list of categories
    Category.print_categories()

def generate_products():
    # create the objects
    pr1 = Product(1, Category.lst_categories[0], 
                  "nike black shoes", "footwear for men", 30.0)
    pr2 = Product(2, Category.lst_categories[0], 
                  "pink havaianas", "footwear for women", 9.50)
    pr3 = Product(3, Category.lst_categories[0], 
                  "brown boots", "footwear for men", 55.0)
    pr4 = Product(4, Category.lst_categories[1],
                  "black jacket", "clothes for men", 110.0)
    pr5 = Product(4, Category.lst_categories[2], 
                  "full stack django and react", "packt pub book", 39.0)
    pr6 = Product(5, Category.lst_categories[2], 
                  "deep learning with tensorflow and keras", "packt pub book", 29.0)

    # print the list of products
    Product.print_products()

def generate_suppliers():
    # create the objects
    sup1 = Supplier(4, "Karina", "karina@gmail.com")    
    sup2 = Supplier(5, "Fernando", "fernando@gmail.com")

    # print list of suppliers
    Supplier.print_suppliers()

def generate_orders():
    # create order1 with detail
    ord1 = Order("A001", [
        OrderDetail(Product.lst_products[0], 10),
        OrderDetail(Product.lst_products[1], 2),
        OrderDetail(Product.lst_products[3], 1)
    ], Supplier.lst_suppliers[0])

    ord1.calculate_total()

    # create order2 with detail
    ord2 = Order("A002", [
        OrderDetail(Product.lst_products[0], 2),
        OrderDetail(Product.lst_products[1], 3),
        OrderDetail(Product.lst_products[2], 10)
    ], Supplier.lst_suppliers[1])

    ord2.calculate_total()

    # create order 3 with detail
    ord3 = Order("A003", [
        OrderDetail(Product.lst_products[1], 5)
    ], Supplier.lst_suppliers[0])

    ord3.calculate_total()

    # create order 4 with detail
    ord4 = Order("A004", [
        OrderDetail(Product.lst_products[1], 2),
        OrderDetail(Product.lst_products[2], 2),
        OrderDetail(Product.lst_products[5], 4)
    ], Supplier.lst_suppliers[1])

    ord4.calculate_total()

    # create order 5 with detail
    ord5 = Order("A005", [
        OrderDetail(Product.lst_products[2], 10),
        OrderDetail(Product.lst_products[4], 2)
    ], Supplier.lst_suppliers[1])

    ord5.calculate_total()

    # insert orders corresponding with supplier 
    for supplier in Supplier.lst_suppliers:
        Supplier.insert_orders(supplier)
        Supplier.print_supplier_orders(supplier)

def main():
    # function to insert persons
    generate_person()

    # function to insert categories
    generate_category()
    
    # function to insert products
    generate_products()

    # function to print products by category
    Product.print_category_products()

    # function to insert suppliers
    generate_suppliers()

    # generate order with detail
    generate_orders()

    # print suppliers again with all register orders
    Supplier.print_suppliers()

    # print all orders
    Order.print_orders()

if __name__ == "__main__":
    main()

