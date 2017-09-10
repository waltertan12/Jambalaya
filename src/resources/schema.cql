
CREATE KEYSPACE IF NOT EXISTS jambalaya WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 };

USE jambalaya;

CREATE TABLE IF NOT EXISTS users (
  id uuid,
  username text,
  password text,
  roles list<text>,
  email text,
  join_date timestamp,
  last_modified timestamp,
  primary key ((id))
);
