CREATE TABLE `course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `exam` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `cost` int DEFAULT NULL,
  `score` int DEFAULT NULL,
  `detail` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_id` int DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `title` text,
  `answer` varchar(10) DEFAULT NULL,
  `tag` tinytext,
  `parent_id` int NOT NULL DEFAULT '0',
  `options` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `correct_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `subject_id` int DEFAULT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `learning_process` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  `sequence` int DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;