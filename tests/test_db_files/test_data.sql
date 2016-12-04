INSERT INTO staff  VALUES
('14334', 'D', 'Phil McGraw', 'RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'),
('14479', 'D', 'Mehmet Oz', 'Q|Fcff{', 'KNqxgHcmgOgfkekpg'), --'PugLove8', 'These Need Hashing'),
('37225', 'N', 'Nurse Joy', 'Lq{3', 'Lq{345'), --'Joy1', 'Joy123'),
('63185', 'A', 'Abraham Jeffers', 'Lgtkejq', 'sygtv{'); --'Jericho', 'qwerty'),

INSERT INTO patients VALUES
('15384','Angelina Jolie','18-39','123-120 ST, Edmonton, Alberta','7801234567','7801234567'),
('20195','Donald Trump','60-99','23-56 ST, Toronto, Ontario','4162347894','4162347894');

INSERT INTO charts VALUES
('10001', '15384', "2015-01-06 12:24:56", "2015-02-13 10:35:42"),
('10008', '20195', "2014-07-12 05:45:16", "2014-07-24 03:03:24");

INSERT INTO symptoms VALUES
("15384", '10001', '37225', "2015-01-08 18:22:55", "Nausea"),
('20195', '10008', '37225', "2014-07-16 15:32:28", "Lymph Swelling");

INSERT INTO diagnoses VALUES
("15384", '10001', '14334', "2015-01-11 14:06:01", "Ebola"),
('20195', '10008', '14334', "2014-07-17 00:39:55", "AIDS");

INSERT INTO medications VALUES
("15384", '10001', '14334', "2015-01-12 02:20:09", "2015-01-12 19:50:32", "2015-02-21 02:51:33", "8", "ZMapp"),
('20195', '10008', '14479', "2014-07-18 04:25:14", "2014-07-19 06:22:09", "2014-10-20 18:26:21", "85", "Retrovir");

INSERT INTO reportedallergies VALUES
("15384", "Tamiflu");

INSERT INTO drugs VALUES
("ZMapp", "anti-Ebola"),
("Viread", "NNRTI"),
("Tamiflu", "anti-viral"),
("Retrovir", "NNRTI");

INSERT INTO dosage VALUES
("ZMapp", "18-39", "8"),
("ZMapp", "40-59", "12"),
("ZMapp", "60-99", "16"),
("Retrovir", "18-39", "75"),
("Retrovir", "40-59", "85"),
("Retrovir", "60-99", "85");

INSERT INTO inferredallergies VALUES
("Viread", "Alkeran");