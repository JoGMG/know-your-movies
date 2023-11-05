-- Prepares the MySQL server for this project
CREATE DATABASE IF NOT EXISTS kym_db;
CREATE USER IF NOT EXISTS 'kym'@'localhost' IDENTIFIED BY 'kym_pwd';
GRANT ALL PRIVILEGES ON `kym_db`.* TO 'kym'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'kym'@'localhost';
FLUSH PRIVILEGES;
