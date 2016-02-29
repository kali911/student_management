CREATE TABLE `Classroom` (
  `classroom_name` varchar(10) NOT NULL,
  `major_id` int(11) NOT NULL,
  PRIMARY KEY (`classroom_name`),
  KEY `Classroom_632501ce` (`major_id`),
  FOREIGN KEY (`major_id`) REFERENCES `Major` (`id`)
)CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `Course` (
  `course_id` varchar(10) NOT NULL,
  `course_name` varchar(10) NOT NULL,
  `property` varchar(10) NOT NULL CHECK (`property` IN ('必修', '选修')),
  `teach_time` varchar(10) NOT NULL,
  `credit` double NOT NULL,
  `teacher` varchar(10) NOT NULL,
  `classroom_name` varchar(10) NOT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE KEY `Course_teacher_uniq` (`teacher`,`classroom_name`),
  KEY `Course_6ed6667d` (`classroom_name`),
  FOREIGN KEY (`classroom_name`) REFERENCES `Classroom` (`classroom_name`)
)CHARSET=utf8 COLLATE=utf8_unicode_ci;




CREATE TABLE `CourseScore` (
  `score` int(11) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `student_id` varchar(15) NOT NULL,
  PRIMARY KEY (`student_id`,`course_id`),
  KEY `CourseScore_ea134da7` (`course_id`),
  KEY `CourseScore_30a811f6` (`student_id`),
  FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`),
  FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`)
)CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `Major` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `major_name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
)CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `Student` (
  `student_id` varchar(15) NOT NULL,
  `student_name` varchar(10) NOT NULL,
  `gender` varchar(2) NOT NULL CHECK (`gender` IN ('男', '女') ),
  `birthday` varchar(10) NOT NULL,
  `classroom_name` varchar(10) NOT NULL,
  PRIMARY KEY (`student_id`),
  KEY `Student_6ed6667d` (`classroom_name`),
  FOREIGN KEY (`classroom_name`) REFERENCES `Classroom` (`classroom_name`)
)CHARSET=utf8 COLLATE=utf8_unicode_ci;
