DROP DATABASE IF EXISTS db2019;
CREATE DATABASE db2019 charset=utf8;
USE db2019;

CREATE TABLE tasks (
  task_id INTEGER NOT NULL AUTO_INCREMENT,
  user_id CHAR(7) NOT NULL,
  content TEXT NOT NULL,
  _limit CHAR(10) NOT NULL,
  PRIMARY KEY (task_id)
);

CREATE TABLE students (
  user_id CHAR(7) NOT NULL,
  password VARCHAR(255) NOT NULL,
  report_count INTEGER NOT NULL,
  is_allowed_to_add_schedule NOT NULL,
  msg_from_admin TEXT,
  PRIMARY KEY (user_id)
);

INSERT INTO tasks(user_id, password, report_count, is_allowed_to_add_schedule, msg_from_admin) values("17fi023", "17fi023", 0, 0, "");
INSERT INTO tasks(user_id, password, report_count, is_allowed_to_add_schedule, msg_from_admin) values("17fi084", "17fi084", 0, 0, "");
INSERT INTO tasks(user_id, password, report_count, is_allowed_to_add_schedule, msg_from_admin) values("17fi088", "17fi088", 0, 0, "");
INSERT INTO tasks(user_id, password, report_count, is_allowed_to_add_schedule, msg_from_admin) values("17fi102", "17fi102", 0, 0, "");

INSERT INTO tasks(user_id, content, _limit) values("17fi023", "complete the documents", "01/14/2020");
INSERT INTO tasks(user_id, content, _limit) values("17fi084", "deploy this program on vps server", "01/14/2020");
INSERT INTO tasks(user_id, content, _limit) values("17fi088", "write codes to make the program", "01/14/2020");
INSERT INTO tasks(user_id, content, _limit) values("17fi102", "manage members", "01/14/2020");
