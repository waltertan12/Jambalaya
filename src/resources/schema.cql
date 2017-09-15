
CREATE DATABASE IF NOT EXISTS jambalaya;

CREATE TABLE IF NOT EXISTS jambalaya.USERS(
    id INT,
    username TEXT,
    password TEXT,
    email TEXT,
    roles TEXT, 
    join_date TIMESTAMP, 
    last_modified TIMESTAMP,
    PRIMARY KEY( id )
);

