-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 03, 2025 at 04:58 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cholosave`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact_us`
--

CREATE TABLE `contact_us` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact_us`
--

INSERT INTO `contact_us` (`id`, `name`, `email`, `description`, `created_at`) VALUES
(1, 'Mashud', 'mamcn', 'fqwascadfa ajbcbabxn ajchanc', '2025-01-02 16:39:49');

-- --------------------------------------------------------

--
-- Table structure for table `group_membership`
--

CREATE TABLE `group_membership` (
  `membership_id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` enum('pending','approved','declined') NOT NULL DEFAULT 'pending',
  `is_admin` tinyint(1) NOT NULL DEFAULT 0,
  `leave_request` enum('pending','approved','declined','no') NOT NULL DEFAULT 'no',
  `join_date` date DEFAULT NULL,
  `join_request_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `group_membership`
--

INSERT INTO `group_membership` (`membership_id`, `group_id`, `user_id`, `status`, `is_admin`, `leave_request`, `join_date`, `join_request_date`) VALUES
(16, 1, 1, 'approved', 0, 'no', NULL, NULL),
(17, 3, 2, 'approved', 1, 'no', '2024-12-31', NULL),
(19, 3, 1, 'declined', 0, 'no', NULL, '2024-12-31'),
(21, 1, 3, 'pending', 0, 'no', NULL, '2025-01-02');

-- --------------------------------------------------------

--
-- Table structure for table `group_points`
--

CREATE TABLE `group_points` (
  `group_id` int(11) NOT NULL,
  `points` int(11) DEFAULT 10,
  `last_updated` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `investments`
--

CREATE TABLE `investments` (
  `investment_id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `investment_type` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `investments`
--

INSERT INTO `investments` (`investment_id`, `group_id`, `amount`, `investment_type`, `created_at`) VALUES
(1, 3, 5000.00, 'Stocks', '2024-12-31 13:04:18');

-- --------------------------------------------------------

--
-- Table structure for table `investment_returns`
--

CREATE TABLE `investment_returns` (
  `return_id` int(11) NOT NULL,
  `investment_id` int(11) DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `return_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `loan_request`
--

CREATE TABLE `loan_request` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `reason` text DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `status` enum('pending','approved','declined') DEFAULT 'pending',
  `return_time` date DEFAULT NULL,
  `approve_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `loan_request`
--

INSERT INTO `loan_request` (`id`, `user_id`, `group_id`, `reason`, `amount`, `status`, `return_time`, `approve_date`) VALUES
(1, 1, 1, 'Medical emergency', 50.00, 'pending', '2024-12-30', NULL),
(2, 1, 1, 'Medical emergency', 50.00, 'pending', '2024-12-30', NULL),
(3, 2, 3, ' emergency', 100.00, 'approved', '2024-12-30', '2024-12-31'),
(4, 1, 3, ' emergency', 100.00, 'approved', '2024-12-30', '2024-12-31'),
(5, 1, 3, 'For Test Purpose', 100.00, 'pending', '2024-12-30', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `my_group`
--

CREATE TABLE `my_group` (
  `group_id` int(11) NOT NULL,
  `group_name` varchar(255) DEFAULT NULL,
  `group_admin_id` int(11) DEFAULT NULL,
  `dps_type` enum('weekly','monthly') DEFAULT NULL,
  `time_period` int(11) DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `goal_amount` int(11) DEFAULT NULL,
  `warning_time` int(11) DEFAULT NULL,
  `emergency_fund` decimal(8,2) DEFAULT NULL,
  `bKash` varchar(255) DEFAULT NULL,
  `Rocket` varchar(255) DEFAULT NULL,
  `Nagad` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `my_group`
--

INSERT INTO `my_group` (`group_id`, `group_name`, `group_admin_id`, `dps_type`, `time_period`, `amount`, `start_date`, `goal_amount`, `warning_time`, `emergency_fund`, `bKash`, `Rocket`, `Nagad`, `created_at`, `description`) VALUES
(1, 'Saving Group', 1, 'weekly', 12, 5000.50, '0000-00-00', 60000, 5, 1000.75, '01712345678', '01787654321', '', '2024-12-28 13:58:03', 'This is a group for saving together.'),
(3, 'Test Group', 2, 'monthly', 12, 5000.50, '0000-00-00', 60000, 5, 900.00, '01712345678', '01787654321', '', '2024-12-31 12:03:26', 'This is a group for saving.');

-- --------------------------------------------------------

--
-- Table structure for table `polls`
--

CREATE TABLE `polls` (
  `poll_id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `poll_question` text DEFAULT NULL,
  `status` enum('active','closed') DEFAULT 'active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `polls`
--

INSERT INTO `polls` (`poll_id`, `group_id`, `poll_question`, `status`, `created_at`) VALUES
(25, 1, 'A user wants to join the group. Do you approve?', 'active', '2025-01-02 11:41:36');

-- --------------------------------------------------------

--
-- Table structure for table `polls_vote`
--

CREATE TABLE `polls_vote` (
  `vote_id` int(11) NOT NULL,
  `poll_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `vote_option` enum('yes','no') NOT NULL,
  `voted_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `question_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `body` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `replies`
--

CREATE TABLE `replies` (
  `reply_id` int(11) NOT NULL,
  `question_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `body` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `savings`
--

CREATE TABLE `savings` (
  `savings_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `savings`
--

INSERT INTO `savings` (`savings_id`, `user_id`, `group_id`, `amount`, `created_at`) VALUES
(1, 1, 1, 1233.00, '2024-12-29 16:09:13'),
(2, 1, 1, 1988.00, '2024-12-31 12:27:13');

-- --------------------------------------------------------

--
-- Table structure for table `transaction_info`
--

CREATE TABLE `transaction_info` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `amount` decimal(8,2) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `payment_method` enum('bKash','Rocket','Nagad') NOT NULL,
  `payment_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` enum('user','group_admin','admin') NOT NULL DEFAULT 'user',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `phone_number`, `password`, `role`, `created_at`) VALUES
(1, 'Irfan', 'a@gmail.com', '1234567890', '$2y$10$0A01GwGgntmaBoLiyYDSyebpakQTJwL9vBKSKeWzkHLuioD6yqMo2', 'user', '2024-12-28 13:55:01'),
(2, 'Void', 'v@gmail.com', '01928346749', '$2y$10$FGhgkqtlDwCRivR2IasUguXqC3Bzy74floaHT7E4oMZSkGWuHuS3e', 'user', '2024-12-31 11:52:43'),
(3, 'X', 'x@gmail.com', '01928346749', '$2y$10$nUjWuSIF5Ecmrj0ehcDwwun5Nx6nLGF.0XK/4CD5M5O9nYaKUriem', 'user', '2025-01-02 11:02:03'),
(5, 'K', 'k@gmail.com', '01928346749', '$2y$10$1XS4MTEvfHXPs64ZWnBgpucH1uIJr0tIOkibMGVo.z0/UVZCqd.ue', 'admin', '2025-01-02 16:38:59');

-- --------------------------------------------------------

--
-- Table structure for table `withdrawal`
--

CREATE TABLE `withdrawal` (
  `withdrawal_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `status` enum('pending','approved','decline') NOT NULL DEFAULT 'pending',
  `request_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact_us`
--
ALTER TABLE `contact_us`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_membership`
--
ALTER TABLE `group_membership`
  ADD PRIMARY KEY (`membership_id`),
  ADD KEY `fk_group_membership_group` (`group_id`),
  ADD KEY `fk_group_membership_user` (`user_id`);

--
-- Indexes for table `group_points`
--
ALTER TABLE `group_points`
  ADD PRIMARY KEY (`group_id`);

--
-- Indexes for table `investments`
--
ALTER TABLE `investments`
  ADD PRIMARY KEY (`investment_id`),
  ADD KEY `fk_investments_group` (`group_id`);

--
-- Indexes for table `investment_returns`
--
ALTER TABLE `investment_returns`
  ADD PRIMARY KEY (`return_id`),
  ADD KEY `fk_investment_returns_investment` (`investment_id`);

--
-- Indexes for table `loan_request`
--
ALTER TABLE `loan_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `group_id` (`group_id`);

--
-- Indexes for table `my_group`
--
ALTER TABLE `my_group`
  ADD PRIMARY KEY (`group_id`),
  ADD KEY `fk_group_admin` (`group_admin_id`);

--
-- Indexes for table `polls`
--
ALTER TABLE `polls`
  ADD PRIMARY KEY (`poll_id`),
  ADD KEY `group_id` (`group_id`);

--
-- Indexes for table `polls_vote`
--
ALTER TABLE `polls_vote`
  ADD PRIMARY KEY (`vote_id`),
  ADD UNIQUE KEY `unique_vote` (`poll_id`,`user_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`question_id`),
  ADD KEY `fk_questions_user` (`user_id`);

--
-- Indexes for table `replies`
--
ALTER TABLE `replies`
  ADD PRIMARY KEY (`reply_id`),
  ADD KEY `fk_replies_question` (`question_id`),
  ADD KEY `fk_replies_user` (`user_id`);

--
-- Indexes for table `savings`
--
ALTER TABLE `savings`
  ADD PRIMARY KEY (`savings_id`),
  ADD KEY `fk_savings_user` (`user_id`),
  ADD KEY `fk_savings_group` (`group_id`);

--
-- Indexes for table `transaction_info`
--
ALTER TABLE `transaction_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_transaction_info_user` (`user_id`),
  ADD KEY `fk_transaction_info_group` (`group_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `withdrawal`
--
ALTER TABLE `withdrawal`
  ADD PRIMARY KEY (`withdrawal_id`),
  ADD KEY `fk_withdrawal_user` (`user_id`),
  ADD KEY `fk_withdrawal_group` (`group_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact_us`
--
ALTER TABLE `contact_us`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `group_membership`
--
ALTER TABLE `group_membership`
  MODIFY `membership_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `investments`
--
ALTER TABLE `investments`
  MODIFY `investment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `investment_returns`
--
ALTER TABLE `investment_returns`
  MODIFY `return_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_request`
--
ALTER TABLE `loan_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `my_group`
--
ALTER TABLE `my_group`
  MODIFY `group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `polls`
--
ALTER TABLE `polls`
  MODIFY `poll_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `polls_vote`
--
ALTER TABLE `polls_vote`
  MODIFY `vote_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `replies`
--
ALTER TABLE `replies`
  MODIFY `reply_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `savings`
--
ALTER TABLE `savings`
  MODIFY `savings_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transaction_info`
--
ALTER TABLE `transaction_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `withdrawal`
--
ALTER TABLE `withdrawal`
  MODIFY `withdrawal_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `group_membership`
--
ALTER TABLE `group_membership`
  ADD CONSTRAINT `fk_group_membership_group` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`),
  ADD CONSTRAINT `fk_group_membership_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `group_points`
--
ALTER TABLE `group_points`
  ADD CONSTRAINT `fk_group_points_group` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`);

--
-- Constraints for table `investments`
--
ALTER TABLE `investments`
  ADD CONSTRAINT `fk_investments_group` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`);

--
-- Constraints for table `investment_returns`
--
ALTER TABLE `investment_returns`
  ADD CONSTRAINT `fk_investment_returns_investment` FOREIGN KEY (`investment_id`) REFERENCES `investments` (`investment_id`);

--
-- Constraints for table `loan_request`
--
ALTER TABLE `loan_request`
  ADD CONSTRAINT `loan_request_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `loan_request_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`);

--
-- Constraints for table `my_group`
--
ALTER TABLE `my_group`
  ADD CONSTRAINT `fk_group_admin` FOREIGN KEY (`group_admin_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `polls`
--
ALTER TABLE `polls`
  ADD CONSTRAINT `polls_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`);

--
-- Constraints for table `polls_vote`
--
ALTER TABLE `polls_vote`
  ADD CONSTRAINT `polls_vote_ibfk_1` FOREIGN KEY (`poll_id`) REFERENCES `polls` (`poll_id`),
  ADD CONSTRAINT `polls_vote_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `fk_questions_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `replies`
--
ALTER TABLE `replies`
  ADD CONSTRAINT `fk_replies_question` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  ADD CONSTRAINT `fk_replies_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `savings`
--
ALTER TABLE `savings`
  ADD CONSTRAINT `fk_savings_group` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`),
  ADD CONSTRAINT `fk_savings_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `transaction_info`
--
ALTER TABLE `transaction_info`
  ADD CONSTRAINT `fk_transaction_info_group` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`),
  ADD CONSTRAINT `fk_transaction_info_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `withdrawal`
--
ALTER TABLE `withdrawal`
  ADD CONSTRAINT `fk_withdrawal_group` FOREIGN KEY (`group_id`) REFERENCES `my_group` (`group_id`),
  ADD CONSTRAINT `fk_withdrawal_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
