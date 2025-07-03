-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jul 03, 2025 at 04:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myntra`
--

-- --------------------------------------------------------

--
-- Table structure for table `carttable1`
--

CREATE TABLE `carttable1` (
  `cart_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_image` varchar(255) DEFAULT NULL,
  `product_price` decimal(10,2) NOT NULL,
  `stock` int(11) DEFAULT 0,
  `quantity` int(11) NOT NULL DEFAULT 1,
  `added_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `carttable1`
--

INSERT INTO `carttable1` (`cart_id`, `product_id`, `user_id`, `product_name`, `product_image`, `product_price`, `stock`, `quantity`, `added_at`) VALUES
(2, 2, 1, 'Bangles', 'bangles.jpg', 265.00, 12, 1, '2025-07-01 19:27:41'),
(3, 4, 1, 'PRINCESS CUT GLITERRING FROCK', 'kids.webp', 1299.00, 1, 1, '2025-07-01 19:27:55');

-- --------------------------------------------------------

--
-- Table structure for table `ordertable`
--

CREATE TABLE `ordertable` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `product_price` decimal(10,2) DEFAULT NULL,
  `product_image` varchar(255) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `delivery_address` text DEFAULT NULL,
  `payment` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ordertable`
--

INSERT INTO `ordertable` (`order_id`, `user_id`, `product_id`, `product_name`, `product_price`, `product_image`, `quantity`, `total_price`, `delivery_address`, `payment`, `status`, `created_at`) VALUES
(1, 1, 1, 'KANCHIPURAM SILK SAREE', 799.00, 'saree1.jpeg', 1, 799.00, '123, Main Road, Chennai', 'COD', 'pending', '2025-06-30 20:56:20');

-- --------------------------------------------------------

--
-- Table structure for table `producttable`
--

CREATE TABLE `producttable` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) DEFAULT 0,
  `image` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `producttable`
--

INSERT INTO `producttable` (`id`, `name`, `price`, `stock`, `image`, `description`, `category`, `created_at`) VALUES
(1, 'KANCHIPURAM SILK SAREE', 799.00, 34, 'saree1.jpeg', ' The designer saree give the Most elegant look ', 'Women', '2025-06-30 20:49:24'),
(2, 'BANGLES', 265.00, 12, 'bangles.jpg', ' A mix of classic and contemporary designs, often incorporating traditional elements with modern materials and styles. ', 'Women', '2025-07-01 19:23:28'),
(3, 'OFFICE SHIRT', 655.00, 23, 'shirt.webp', 'A garment for the upper part of the body usually with a collar, sleeves, a front opening, and a tail long enough to be tucked inside pants or a skirt.', 'Men', '2025-07-01 19:25:52'),
(4, 'PRINCESS CUT GLITERRING FROCK', 1299.00, 1, 'kids.webp', 'Frocks are often designed for special occasions like parties, weddings, or other celebrations, and they come in various styles, colors, and lengths. ', 'Women', '2025-07-01 19:27:30');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `emailid` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `emailid`, `password`) VALUES
(1, 'Reethu krishna', 'reethu@2004', 'reethu@2004'),
(4, 'Kutty', 'Kutty@2004', 'kutty@2004'),
(18, 'Krishna', 'Krishna@2004', 'Krish@2004');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `carttable1`
--
ALTER TABLE `carttable1`
  ADD PRIMARY KEY (`cart_id`);

--
-- Indexes for table `ordertable`
--
ALTER TABLE `ordertable`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `producttable`
--
ALTER TABLE `producttable`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `emailid` (`emailid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `carttable1`
--
ALTER TABLE `carttable1`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `ordertable`
--
ALTER TABLE `ordertable`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `producttable`
--
ALTER TABLE `producttable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
