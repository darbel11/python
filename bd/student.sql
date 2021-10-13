CREATE TABLE programs(
	id integer primary key autoincrement not null,
	
	name varchar(100) not null
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE students(
	id integer primary key autoincrement not null,
	program_id integer not null,

	card varchar(10) not null,

	surname varchar(20) not null,
	name varchar(20) not null,
	patronymic varchar(20) null,
	
	foreign key(program_id) references programs(id)
);
CREATE TABLE courses(
	id integer primary key autoincrement not null,
	name varchar(200) not null
);
CREATE TABLE programs_courses(
	semester_number int not null,
	course_id int not null,
	program_id int not null,
	
	primary key(semester_number, course_id, program_id),
	foreign key(course_id) references courses(id),
	foreign key(program_id) references programs(id)
);
;
CREATE TABLE marks(
	student_id int not null,
	course_id int not null,
	mark int not null,
	
	primary key(course_id, student_id),
	foreign key(student_id) references students(id),
	foreign key(course_id) references courses(id)
);
;
CREATE UNIQUE INDEX students_card on students(card);
CREATE INDEX students_names on students(surname, name, patronymic);
