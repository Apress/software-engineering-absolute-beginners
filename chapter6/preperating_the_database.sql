-- Adminer 4.7.2 MySQL dump
-- These steps are not in the chapter, the chapter required creating the DB with Adminer
SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `cities`;
CREATE TABLE `cities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `cities` (`id`, `city`) VALUES
(1,	'london'),
(2,	'hove'),
(3,	'brighton');

DROP TABLE IF EXISTS `client_languages`;
CREATE TABLE `client_languages` (
  `client_id` int NOT NULL,
  `language_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `client_languages` (`client_id`, `language_id`) VALUES
(1,	2),
(1,	1),
(2,	2),
(2,	3),
(3,	2);

DROP TABLE IF EXISTS `clients`;
CREATE TABLE `clients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `salutation_id` int NOT NULL,
  `surname` varchar(50) NOT NULL,
  `mobile` varchar(12) NOT NULL,
  `city_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `clients` (`id`, `salutation_id`, `surname`, `mobile`, `city_id`) VALUES
(1,	1,	'Kruger',	'0865214459',	1),
(2,	2,	'Jane',	'45678912',	1),
(3,	1,	'De Wet',	'987654321',	3),
(4,	3,	'Loubser',	'65412365',	2),
(5,	2,	'Theron',	'7984132',	2),
(6,	1,	'Stander',	'654321654',	2);

DROP TABLE IF EXISTS `languages`;
CREATE TABLE `languages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `languages` (`id`, `language`) VALUES
(1,	'German'),
(2,	'English'),
(3,	'French');

DROP TABLE IF EXISTS `salutations`;
CREATE TABLE `salutations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `salutation` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `salutations` (`id`, `salutation`) VALUES
(1,	'Mr'),
(2,	'Miss'),
(3,	'Mrs');

-- 2020-08-31 16:14:05


