CREATE DATABASE libraryPyDb;
USE libraryPyDb;

CREATE TABLE Book(
	id int auto_increment,
    title varchar(100) not null,
    author varchar(100) not null,
    status bool default 0 not null,
    CONSTRAINT PK_Book PRIMARY KEY (id)
);
-- Available = 0 || Issued: 1

-- Insertion examples:
INSERT INTO Book(title, author, status) VALUES ('The Psychology of Money', 'Morgan Housel', 0);
INSERT INTO Book(title, author, status) VALUES ('The Hobbit', 'J. R. R. Tolkien', 0);
INSERT INTO Book(title, author, status) VALUES ('The Eye Of The World', 'Robert Jordan', 1);

DROP TABLE Book;