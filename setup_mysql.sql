-- prepares a MySQL server for the CrossMe project

CREATE DATABASE IF NOT EXISTS craftiny;
CREATE USER IF NOT EXISTS 'craft_user'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON craftiny.* TO 'craft_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'craft_user'@'localhost';
FLUSH PRIVILEGES;