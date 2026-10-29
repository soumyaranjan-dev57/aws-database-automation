CREATE DATABASE IF NOT EXISTS aws;
USE aws;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO students (id, name)
VALUES (1, 'Soumya'), (2, 'Barik');

SELECT * FROM students;

DELETE FROM students
WHERE id = 2;

SELECT * FROM students;