# procedures and views for person
use db_sales;

#	 			--- table person ---

# view to list person
create view v_person as 
select p.id_person, p.name, p.email, c.name as company, tp.description as des_type
from person p
inner join company c 
on p.Company_id_company = c.id_company
inner join typeperson tp
on p.TypePerson_id_type_person = tp.id_type_person;

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
