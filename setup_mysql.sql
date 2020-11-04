-- prepares a MySQL server for the craftiiny project

CREATE DATABASE IF NOT EXISTS craftiny_v1;
CREATE USER IF NOT EXISTS 'craft_user_v1'@'localhost' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON craftiny_v1.* TO 'craft_user_v1'@'localhost';
GRANT SELECT ON performance_schema.* TO 'craft_user_v1'@'localhost';
FLUSH PRIVILEGES;
