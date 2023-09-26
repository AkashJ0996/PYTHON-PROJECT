create database projpy;
use projpy;

create table login_info(
user_name varchar(20),
password varchar(9));

insert into login_info values ("Akashj","78951@j"),("Mr.abc","abc&@95"),("xyz@mail","49xyz01"),("sitaR15","sitaram"),("jhon92","@jhon92"),("shoaibk","shoaib&k");

select * from login_info;


create table phonebook(
first_name varchar(10),
last_name varchar(10),
phone_num varchar(20));

insert into phonebook values ("Akash","Jadhav","+91 7895123007"),("Abc","Sharma","+91 2025550105"),("Xyz","Raut","+91 7778880102"),
("Sita","Roy","+91 5557879103"),("Jhon","Wick","+91 2228279204"),("Shoaib","Khan","+91 9828457021");

select * from phonebook;







