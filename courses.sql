-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2023 at 07:15 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `institution`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `course_name` varchar(20) NOT NULL,
  `core_subject` varchar(20) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `price` varchar(20) NOT NULL,
  `payment_type` varchar(20) NOT NULL,
  `enquiry` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `course_name`, `core_subject`, `duration`, `price`, `payment_type`, `enquiry`) VALUES
(1, 'Server Side Programm', 'Python', '45 days', '7000', 'one time', '9007045632'),
(2, 'Python Express', 'Python', '60 days', '3000', 'one time', '6290121478'),
(3, 'Big Dream in Data Sc', 'Data Science', '90 days', '7000', 'Lump sum', '7894121478'),
(4, 'Train your Computer', 'Machine Learning', '90 days', '8000', 'Lump sum', '9842121478'),
(5, 'Python Jet ', 'Python', '30 days', '1000', 'one time', '6765121478'),
(6, 'C++', 'C++', '60 days', '5000', 'one time', '633421478'),
(7, 'Java to placement', 'Java', '30 days', '8000', 'one time', '7980121478'),
(8, 'Quick Machine Learni', 'Machine Learning', '45 days', '5000', 'one time', '6290121220'),
(9, 'Python with Flask', 'Python', '90 days', '9000', 'Monthly', '6290624578'),
(10, 'Advance Java', 'Java', '120 days', '12000', 'Lumpsum', '8013121478'),
(11, 'Grab Tensor Flow and', 'Python', '60 days', '10000', 'one time', '6290121478'),
(12, 'Core Java', 'Java', '60 days', '4500', 'one time', '9505121478'),
(13, 'Training of Networki', 'Network', '30 days', '3000', 'one time', '9163186478'),
(15, 'Complete Database wi', 'SQL', '60 days', '6000', 'one time', '8207045632');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
