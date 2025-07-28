create database cafeteria
default character set utf8mb4
default collate utf8mb4_general_ci;
Use cafeteria;
create table ordem(
id int auto_increment,
pedido varchar(400) not null,
hora timestamp default current_timestamp,
primary key (id)
) default charset = utf8mb4;
insert into ordem
(pedido)
Values
('1 - Torta de chocolate'),
('2 - Pastel de flango'),
('1 - Cappuccino');

create table barista(
id int auto_increment,
pedidocompl varchar(100) not null,
primary key (id)
)default charset = utf8mb4;
insert into barista (pedidocompl)
Values
('1 - 3x Expresso'),
('1 - 2x Pastel'),
('2 - 1x Cappuccino');


drop table ordem;
select * from ordem;
truncate table ordem;
truncate table barista;
drop table barista;
select * from barista;
select pedidocompl from barista;