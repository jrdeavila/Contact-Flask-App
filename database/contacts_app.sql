        -- TABLES --

create table users(
  id int(10) primary key auto_increment,
  first_name varchar(20) not null,
  last_name varchar(20) not null,
  phone varchar(10) not null,
  username varchar(20) not null,
  password varchar(128) not null
);

create table contacts(
  id int(10) primary key auto_increment,
  fullname varchar(20) not null,
  phone varchar(10) not null,
  email varchar(30) not null,
  added_date datetime not null,
  user_id int(10) not null,
  foreign key (user_id) references users(id)
);


        -- PROCEDURES --

drop procedure if exists add_user;
delimiter $$
create procedure add_user(
    new_name varchar(20),
    new_last_name varchar(20),
    new_phone varchar(10),
    new_username varchar(20),
    new_password varchar(128))
begin
declare exist int;
    set exist = (select count(*) from users where username = new_username and password = new_password);
    if exist = 0 then
        insert into users(first_name, last_name, phone, username, password)
        values(new_name, new_last_name, new_phone, new_username, new_password);
        select('User added successfully');
    else
        select('User already exists');
    end if;
end $$


drop procedure if exists get_user;
delimiter $$
create procedure get_user(g_username varchar(20), g_password varchar(128))
begin
declare records int;
    set records = (select count(*) from users where username = g_username and password = g_password);
    if records > 0 then
        select * from users where username = g_username and password = g_password;
    else
        select('Incorrect username or password');
    end if;
end $$



drop procedure if exists get_contacts;
delimiter $$
create procedure get_contacts(g_user_id int(10))
begin
    select * from contacts where user_id = g_user_id;
end $$

drop procedure if exists add_contact;
delimiter $$
create procedure add_contact(
    new_fullname varchar(30),
    new_phone varchar(10),
    new_email varchar(40),
    new_added_date datetime,
    new_user_id int(10)
)
begin
declare exist int;
    set exist = (select count(*) from contacts where phone = new_phone and user_id = new_user_id);
    if exist = 0 then
        insert into contacts(fullname, phone, email, added_date, user_id)
        values(new_fullname, new_phone, new_email, new_added_date, new_user_id);
        select('Contact added successfully');
    else
        select('This contact already exist');
    end if;
end $$


drop procedure if exists remove_contact;
delimiter $$
create procedure remove_contact(contact_id int(10))
begin
    delete from contacts where id = contact_id;
    select('Contact removed succesfully');
end $$


drop procedure if exists get_contact;
delimiter $$
create procedure get_contact(contact_id int(10))
begin
    select * from contacts where id = contact_id;
end $$


drop procedure if exists update_contact;
delimiter $$
create procedure update_contact(
    new_fullname varchar(30),
    new_phone varchar(10),
    new_email varchar(40),
    contact_id int(10)
)
begin
    update contacts set
        fullname = new_fullname,
        phone = new_phone,
        email = new_email
    where id = contact_id;
    select ('Contact updated successfully');
end $$


