drop table if exists deliveries;
create table deliveries (
    tracking text primary key,
    carrier text not null,
    street_address text not null,
    zipcode text not null
);
