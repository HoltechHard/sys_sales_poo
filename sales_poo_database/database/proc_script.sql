# procedures and views for person
use db_sales;

#		 			--- table person ---

# view to list person
create view vw_person as 
select p.id_person, p.name, p.email, c.name as company, tp.description as des_type
from person p
inner join company c 
on p.Company_id_company = c.id_company
inner join typeperson tp
on p.TypePerson_id_type_person = tp.id_type_person
order by p.id_person asc;

select * from v_person;

# store procedure to insert person
delimiter $$
create procedure sp_person_insert(
	in p_name varchar(255),
    in p_email varchar(45),
    in c_company int,
    in tp_type int
)
begin 
	insert into person(name, email, Company_id_company, TypePerson_id_type_person)
    values(p_name, p_email, c_company, tp_type);
end $$
delimiter ;

call sp_person_insert("Greecy", "greecy@gmail.com", 1, 2);
select * from person;

# store procedure to edit person
delimiter $$
create procedure sp_person_edit(
	in p_id int,
    in p_name varchar(255),
    in p_email varchar(45),
    in c_company int,
    in tp_type int
)
begin
	update person p
		set p.name = p_name, p.email = p_email, p.Company_id_company = c_company, 
			p.TypePerson_id_type_person = tp_type
    where p.id_person = p_id;    
end $$
delimiter ;

call sp_person_edit(9, "Robert", "robert123@gmail.com", 1, 3);
select * from vw_person;

#					--- table supplier ---

# view to list supplier
create view vw_supplier as
select s.Person_id_person, p.name, s.status, s.num_orders, s.acc_all_orders 
from supplier s
inner join person p
on s.Person_id_person = p.id_person
order by s.Person_id_person;

select * from vw_supplier;

# store procedure to insert supplier
delimiter $$
create procedure sp_supplier_insert(
	in p_id int,
    in s_status varchar(45)    
)
begin
	insert into supplier(Person_id_person, status, num_orders, acc_all_orders)
    values(p_id, s_status, 0, 0.0);
end $$
delimiter ;

call sp_supplier_insert(2, "active supplier");

# store procedure to edit supplier
delimiter $$
create procedure sp_supplier_edit(
	in p_id int,
    in s_status varchar(45)
)
begin 
	update supplier s
		set s.status = s_status
	where s.Person_id_person = p_id;
end $$
delimiter ;

call sp_supplier_edit(2, "inactive supplier");

# store procedure to list orders by supplier
delimiter $$
create procedure sp_ord_by_supplier(in s_id int)
begin
	select ord.date_generated, ord.id_order, ord.total
    from `order` ord
    where ord.Supplier_Person_id_person = s_id;
end $$
delimiter ;

call sp_ord_by_supplier(7);

