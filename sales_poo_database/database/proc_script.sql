use db_sales;

#		 			--- table person ---
# procedures and views for person

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
# procedures and views for supplier

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

#				--- table category ---
# procedures and views for category

# view to list category
create view vw_category as
select c.id_category, c.name
from category c
order by c.id_category;

select * from vw_category;

# store procedure to insert category
delimiter $$
create procedure sp_category_insert(in c_name varchar(255))
begin
	insert into category(name) values(c_name);
end $$
delimiter ;

call sp_category_insert("laptops");

# store procedure to edit category
delimiter $$
create procedure sp_category_edit(
	in c_id int,
	in c_name varchar(255)
)
begin
	update category c
		set c.name = c_name
	where c.id_category = c_id;
end $$
delimiter ;

call sp_category_edit(4, "smartphones");

#				--- table brand ---
# procedures and views for brand

# view to list brand
create view vw_brand as 
select b.id_brand, b.name, b.date_creation
from brand b
order by b.id_brand;

select * from vw_brand;

# store procedure to insert brand
delimiter $$
create procedure sp_brand_insert(
	in b_name varchar(255),
    in b_date_creation datetime
)
begin
	insert into brand(name, date_creation)
    values(b_name, b_date_creation);
end $$
delimiter ;

call sp_brand_insert("huawei", "1988-09-15");

# store procedure to edit brand
delimiter $$
create procedure sp_brand_edit(
	in b_id int,
    in b_name varchar(255),
    in b_date_creation datetime
)
begin
	update brand b
		set b.name = b_name, b.date_creation = b_date_creation
    where b.id_brand = b_id;
end $$
delimiter ;

call sp_brand_edit(5, "huawei", "1987-09-15");

#				--- table product ---
# procedures and views for product

# view to list product
create view vw_product as 
select p.id_product, p.bar_code, p.name as prod_name, c.name as cat_name, 
		b.name as brand_name, p.description, p.unit_price
from product p
inner join category c
on p.Category_id_category = c.id_category
inner join brand b
on p.Brand_id_brand = b.id_brand
order by p.id_product;

select * from vw_product;

# store procedure to insert product
delimiter $$
create procedure sp_product_insert(
    in p_bar_code char(12),
    in p_name varchar(255),
    in p_description text(400),
    in p_unit_price decimal(8, 2),
    in c_category int,
    in b_brand int
)
begin
	insert into product(bar_code, name, description, unit_price, 
			Category_id_category, Brand_id_brand) 
	values(p_bar_code, p_name, p_description, p_unit_price, 
			c_category, b_brand);
end $$
delimiter ;

call sp_product_insert("S01-4537-108", "Smartphone Huawei P20", "smartphone huawei",
		1120.0, 4, 5);

# store procedure to edit product
delimiter $$
create procedure sp_product_edit(
	in p_id int, 
    in p_bar_code char(12),
    in p_name varchar(255),
    in p_description text(400),
    in p_unit_price decimal(8, 2),
    in c_category int,
    in b_brand int
)
begin
	update product p
		set p.bar_code = p_bar_code, p.name = p_name, p.description = p_description,
			p.unit_price = p_unit_price, p.Category_id_category = c_category,
            p.Brand_id_brand = b_brand
    where p.id_product = p_id;
end $$
delimiter ;

call sp_product_edit(7, "S02-4555-108", "Smartphone Huawei P20", "smartphone with 3 cameras p20",
		1120.0, 4, 5);

select * from product;

# store procedure to list product by category
delimiter $$
create procedure sp_prod_by_category(in c_id int)
begin
	select p.id_product, p.name, p.unit_price
    from product p
    where p.Category_id_category = c_id
    order by p.id_product;
end $$
delimiter ;

call sp_prod_by_category(1);

select * from category;

