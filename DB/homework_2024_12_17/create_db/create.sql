CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE subjects (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL
);

CREATE TABLE student_subject (
	student_id INT REFERENCES students(id),
	subject_id INT REFERENCES subjects(id),
	PRIMARY KEY (student_id, subject_id)
);

INSERT INTO students (first_name, last_name) VALUES
('Emma', 'Johnson'),
('Liam', 'Smith'),
('Olivia', 'Brown'),
('Noah', 'Williams'),
('Ava', 'Jones'),
('Elijah', 'Garcia'),
('Sophia', 'Martinez'),
('Lucas', 'Rodriguez'),
('Mia', 'Hernandez'),
('Mason', 'Lopez'),
('Isabella', 'Gonzalez'),
('Ethan', 'Wilson'),
('Charlotte', 'Anderson'),
('Aiden', 'Thomas'),
('Amelia', 'Taylor'),
('James', 'Moore'),
('Harper', 'Jackson'),
('Benjamin', 'Lee'),
('Evelyn', 'Harris'),
('Jacob', 'Clark'),
('Ella', 'Lewis'),
('Michael', 'Robinson'),
('Scarlett', 'Walker'),
('Alexander', 'Hall'),
('Grace', 'Allen'),
('Daniel', 'Young'),
('Chloe', 'King'),
('Henry', 'Wright'),
('Lily', 'Scott'),
('Jackson', 'Green');

INSERT INTO subjects (title) VALUES
('DevOps'),
('Developer'),
('QA'),
('PM'),
('BA');

INSERT INTO student_subject (student_id, subject_id) VALUES
(1, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (6, 2), 
(7, 3), (8, 4), (9, 5), (10, 1), (11, 2), (12, 3), (13, 4), 
(14, 5), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5),
(20, 1), (21, 2), (22, 3), (23, 4), (24, 5), (25, 1), (26, 2), 
(27, 3), (28, 4), (29, 5), (30, 1);
