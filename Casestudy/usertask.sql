CREATE TABLE `user` (
  `user_id` int DEFAULT NULL,
  `user_name` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `created_on` varchar(20) DEFAULT NULL,
  `modified_on` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `task` (
  `task_id` int DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `bookmark` varchar(20) DEFAULT NULL,
  `owner_id` int DEFAULT NULL,
  `creator_id` int DEFAULT NULL,
  `created_on` varchar(20) DEFAULT NULL,
  `modified_on` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;