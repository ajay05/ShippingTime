drop table if exists deliveries;
create table deliveries (
    tracking integer primary key,
    carrier text not null,
    street_address text not null,
    zipcode integer not null
);
