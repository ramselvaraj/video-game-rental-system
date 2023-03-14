-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 24, 2021 at 04:49 PM
-- Server version: 5.6.21
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `videogamerental`
--

-- --------------------------------------------------------

--
-- Table structure for table `videogames`
--

CREATE TABLE IF NOT EXISTS `videogame` (
`game_id` int(20) NOT NULL,
  `game_name` varchar(50) NOT NULL,
  `game_img` varchar(50) DEFAULT 'NA',
  `trailer_link` varchar(200) DEFAULT 'NA',
  `price_day` float NOT NULL,
  `game_availability` varchar(10) NOT NULL,
  `platform` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `videogame`
--

INSERT INTO `videogame` (`game_id`, `game_name`, `game_img`,`trailer_link`, `price_day` , `game_availability`, `platform`) VALUES
(1, 'Cyberpunk 2077', 'C:\xampp\htdocs\videogame-rental\assets\img\games\cyberpunk2077.jpg','https://www.youtube.com/embed/BO8lX3hDU30', 399 ,'yes', 'PS4'),
(2, 'Call of Duty : Modern Warfare (2019)', 'C:\xampp\htdocs\videogame-rental\assets\img\games\mw2019.jpg','https://www.youtube.com/embed/bH1lHCirCGI', 399 ,'yes', 'PS4'),
(3, 'Call of Duty : Modern Warfare II (2022)', 'C:\xampp\htdocs\videogame-rental\assets\img\games\mw2019.jpg','https://www.youtube.com/embed/bH1lHCirCGI', 399 ,'yes', 'PS4'),
(4, 'Gears of War', 'C:\xampp\htdocs\videogame-rental\assets\img\games\mw2019.jpg','https://www.youtube.com/embed/bH1lHCirCGI',399 ,'yes', 'Xbox One');

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `customer_username` varchar(50) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `customer_phone` varchar(15) NOT NULL,
  `customer_email` varchar(25) NOT NULL,
  `customer_address` varchar(50) NOT NULL,
  `customer_password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_username`, `customer_name`, `customer_phone`, `customer_email`, `customer_address`, `customer_password`) VALUES
('ramsel', 'Ram Selvaraj', '0785556580', 'ramselvaraj@gmail.com', '2677  Burton Avenue', 'password');

-- --------------------------------------------------------

-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `name` varchar(20) NOT NULL,
  `e_mail` varchar(30) NOT NULL,
  `message` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`name`, `e_mail`, `message`) VALUES
('Ram Selvaraj', 'ramselvaraj@gmail.com', 'Test Feedback.');

-- --------------------------------------------------------

--
-- Table structure for table `rentedgames`
--

CREATE TABLE IF NOT EXISTS `rentedgames` (
`id` int(100) NOT NULL,
  `customer_username` varchar(50) NOT NULL,
  `game_id` int(20) NOT NULL,
  `booking_date` date NOT NULL,
  `rent_start_date` date NOT NULL,
  `rent_end_date` date NOT NULL,
  `game_return_date` date DEFAULT NULL,
  `fare` double NOT NULL,
  `no_of_days` int(50) DEFAULT NULL,
  `total_amount` double DEFAULT NULL,
  `return_status` varchar(10) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=574681260 DEFAULT CHARSET=utf8;

--w
-- Dumping data for table `rentedcars`
--

INSERT INTO `rentedgames` (`id`, `customer_username`, `game_id`, `booking_date`, `rent_start_date`, `rent_end_date`, `game_return_date`, `fare`, `no_of_days`, `total_amount`, `return_status`) VALUES
(574681245, 'ramsel', 2, '2022-11-11', '2022-11-11', '2022-11-13', '2018-11-13', 399, 2, 798, 'R');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `videogame`
--
ALTER TABLE `videogame`
 ADD PRIMARY KEY (`game_id`);
--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
 ADD PRIMARY KEY (`customer_username`);

--
--
-- Indices for table `rentedgames`
--
ALTER TABLE `rentedgames`
 ADD PRIMARY KEY (`id`), ADD KEY `customer_username` (`customer_username`), ADD KEY `game_id` (`game_id`);

--
-- AUTO_INCREMENT for table `videogame` - Creating new Game ID's
--
ALTER TABLE `videogame`
MODIFY `game_id` int(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `rentedgames` - Creating new Rent ID's 
--
ALTER TABLE `rentedgames`
MODIFY `id` int(100) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=574681260;
--
--
-- Constraints for table `rentedgames` - Adding constraints to make sure game id and customer usernames are correct
--
ALTER TABLE `rentedgames`
ADD CONSTRAINT `rentedgames_ibfk_1` FOREIGN KEY (`customer_username`) REFERENCES `customers` (`customer_username`),
ADD CONSTRAINT `rentedgames_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `videogame` (`game_id`);


DELIMITER $$
CREATE TRIGGER `add_img` BEFORE INSERT ON `videogame` FOR
EACH ROW BEGIN
if NEW.platform = "PS4" then SET NEW.platform_img = "assets/img/platform/ps4.jpg"; end if;
if NEW.platform = "Xbox One" then SET NEW.platform_img = "assets/img/platform/xbox.jpg"; end if;
END
$$
