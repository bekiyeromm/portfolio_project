CREATE DATABASE IF NOT EXISTS pims_db;
CREATE USER IF NOT EXISTS 'pims_user'@'localhost' IDENTIFIED BY 'pims_user_pwd';
GRANT ALL PRIVILEGES ON `pims_db`.* TO 'pims_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pims_user'@'localhost';
FLUSH PRIVILEGES;
