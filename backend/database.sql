-- prepares a MySQL server for the project
--create db name and user
CREATE DATABASE IF NOT EXISTS `twitter`;
CREATE USER IF NOT EXISTS 'crud'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
GRANT ALL PRIVILEGES ON `twitter`.* TO 'crud'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'crud'@'localhost';
FLUSH PRIVILEGES;

-- Accounts
CREATE TABLE accounts (
  id INT NOT NULL AUTO_INCREMENT,
  fullname VARCHAR(50) NOT NULL,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  profile_pic VARCHAR(255), -- Assuming storing the file path
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    tweet TEXT,
    fullname VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    post_pic VARCHAR(255),
    profile_pic VARCHAR(255),-- Assuming the file path or URL of the post picture will be stored
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES accounts(id)
);
