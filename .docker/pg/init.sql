CREATE TABLE users
(
    email  VARCHAR(256) UNIQUE NOT NULL,
    "name" VARCHAR(256)        NOT NULL
);

CREATE OR REPLACE FUNCTION hello(name varchar(100))
    RETURNS VARCHAR AS
$$
BEGIN
    RETURN 'Hello ' || name;

END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION hello2(name varchar(100), OUT name2 varchar(100))
    RETURNS RECORD AS
$$
BEGIN
    name2 := 'Hello ' || name;
    return;
END;
$$
LANGUAGE plpgsql;
