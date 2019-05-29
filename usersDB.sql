-- Database: "pythonProject"

-- DROP DATABASE "pythonProject";

CREATE DATABASE "pythonProject"
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Russian_Russia.1251'
       LC_CTYPE = 'Russian_Russia.1251'
       CONNECTION LIMIT = -1;

CREATE TABLE userDB(
login varchar(20),
passw varchar(20)
);