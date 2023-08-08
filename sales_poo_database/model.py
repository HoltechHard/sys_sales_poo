# models

from mysqldb import mysql_cnn

# class Person

class Person:

    # list person
    def list_person():
        mysql_cnn.connect()
        query = "select * from v_person"
        res = mysql_cnn.execute_query(query)
        print("List of persons:")
        for row in res:
            print(f"id: {row[0]} | name: {row[1]} | email: {row[2]} | "
                  f"company: {row[3]} | type: {row[4]}")
        mysql_cnn.close()

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

def main():
    Person.insert_person("Roberto", "roberto@gmail.com", 1, 2)
    Person.list_person()

if __name__ == "__main__":
    main()

