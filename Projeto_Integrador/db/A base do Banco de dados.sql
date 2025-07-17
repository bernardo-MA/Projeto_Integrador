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
mesa int not null,
pedidocompl varchar(100) not null,
primary key (id)
)default charset = utf8mb4;



drop table ordem;
select * from ordem;
select * from ordem where mesa = 1;
truncate table ordem;
