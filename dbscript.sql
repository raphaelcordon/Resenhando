CREATE DATABASE IF NOT EXISTS music_school;

CREATE USER IF NOT EXISTS 'music_school'@'localhost' IDENTIFIED BY 'Music_school123';
GRANT DELETE, INSERT, SELECT, UPDATE ON music_school.* TO 'music_school'@'localhost';

# Creating tables in the 'music_school' database:
USE music_school;
CREATE TABLE IF NOT EXISTS course (
						ID INTEGER AUTO_INCREMENT PRIMARY KEY,
						NAME VARCHAR(50)
						);

CREATE TABLE IF NOT EXISTS users (
						ID INTEGER AUTO_INCREMENT UNIQUE KEY,
                        USERNAME VARCHAR(30),
						NAME VARCHAR(50),
                        password VARCHAR(255),
						COURSE BOOL,
						ACCESS_LEVEL VARCHAR(20)
						);

CREATE TABLE IF NOT EXISTS enrolled_courses (
						STUDENT_ID SMALLINT not null,
                        COURSE_ID SMALLINT not null
                        );

CREATE TABLE IF NOT EXISTS classes (
						ID INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE KEY,
						COURSE_ID SMALLINT,
						INSTRUCTOR_ID SMALLINT,
						STUDENT_ID SMALLINT,
						CALENDAR DATE
						);

# Creating users with different Access Levels to test

INSERT INTO users (Name, pass, Course, Access_level)
		VALUES ('admin', Sha2('admin',512), false, 'master');

INSERT INTO users (Name, pass, Course, Access_level)
		VALUES ('teacher', Sha2('teacher',512), false, 'instructor');

INSERT INTO users (Name, pass, Course, Access_level)
		VALUES ('student', Sha2('student',512), false, 'student');



