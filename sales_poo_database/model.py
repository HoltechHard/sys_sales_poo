# models

from mysqldb import mysql_cnn

# class Person

class Person:

    # list person
    def list_person():
        mysql_cnn.connect()
        query = "select * from vw_person"
        res = mysql_cnn.execute_query(query)        
        mysql_cnn.close()

        return res

    # print person
    def print_person(result):
        print("List of persons: ")
        for row in result:
            print(f"id: {row[0]} | name: {row[1]} | email: {row[2]} | "
                  f"company: {row[3]} | type: {row[4]}")

    # insert person
    def insert_person(p_name, p_email, c_company, tp_type):
        mysql_cnn.connect()
        procedure = "sp_person_insert"
        res = mysql_cnn.execute_sprocedure(procedure, p_name, p_email, c_company, tp_type)
        mysql_cnn.close()

        if res == 1:
            print("data successfully inserted in table person")
        elif res == 0:
            print("data not inserted")

    # edit person
    def edit_person(p_id, p_name, p_email, c_company, tp_type):
        mysql_cnn.connect()
        procedure = "sp_person_edit"
        res = mysql_cnn.execute_sprocedure(procedure, p_id, p_name, p_email, c_company, tp_type)
        mysql_cnn.close()

        if res == 1:
            print("data successfully edited in table person")
        elif res == 0:
            print("data not edited")


# class Supplier

class Supplier:

    # list supplier
    def list_supplier():
        mysql_cnn.connect()
        query = "select * from vw_supplier"
        res = mysql_cnn.execute_query(query)
        mysql_cnn.close()

        return res

    def print_supplier(result):
        print("List of suppliers: ")
        for row in result:
            print(f"id: {row[0]} | name: {row[1]} | status: {row[2]} | "
                  f"num-orders: {row[3]} | accumulate-orders: {row[4]}")

    # insert supplier
    def insert_supplier(p_id, s_status):
        mysql_cnn.connect()
        procedure = "sp_supplier_insert"
        res = mysql_cnn.execute_sprocedure(procedure, p_id, s_status)
        mysql_cnn.close()

        if res == 1:
            print("data successfully inserted in table supplier")
        elif res == 0:
            print("data not inserted")
    
    # edit supplier
    def edit_supplier(p_id, s_status):
        mysql_cnn.connect()
        procedure = "sp_supplier_edit"
        res = mysql_cnn.execute_sprocedure(procedure, p_id, s_status)
        mysql_cnn.close()

        if res == 1:
            print("data successfully edited in table supplier")
        elif res == 0:
            print("data not edited")

    # list orders by supplier
    def list_ord_by_supplier(s_id):
        mysql_cnn.connect()
        procedure = "sp_ord_by_supplier"
        res = mysql_cnn.execute_procedure_query(procedure, s_id)
        mysql_cnn.close()

        return res

    # print orders by supplier
    def print_ord_by_supplier():
        print(" --- List of orders by supplier --- ")
        ls_suppliers = Supplier.list_supplier()
        # print num orders by supplier
        for sup in ls_suppliers:
            s_id = sup[0]
            print(f"Register of orders for supplier {sup[1]}: ")
            print(f"Status = {sup[2]} | Num-orders = {sup[3]}")
            print("----------------------------------------------------")

            ls_ords = Supplier.list_ord_by_supplier(s_id)

            # print the orders by supplier
            if ls_ords:
                for ord in ls_ords:
                    print(f"date: {ord[0]}   ---  "
                          f"order-id: {ord[1]} ==> total = {ord[2]}")
            else:
                print(f"Supplier {sup[1]} doesnt made orders")

def main():
    # Person.insert_person("Roberto", "roberto@gmail.com", 1, 2)
    # Person.edit_person(9, "Jhon", "jhon@gmail.com", 1, 3)
    persons = Person.list_person()
    Person.print_person(persons)

    # Supplier.insert_supplier(3, "active supplier")
    # Supplier.edit_supplier(3, "innactive supplier")
    suppliers = Supplier.list_supplier()
    Supplier.print_supplier(suppliers)
    Supplier.print_ord_by_supplier()

if __name__ == "__main__":
    main()

