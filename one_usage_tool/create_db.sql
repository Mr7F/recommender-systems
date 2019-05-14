
CREATE USER 'python_user' IDENTIFIED BY 'S3cR37_p@ss0WrD_r@d0|/|';
GRANT ALL ON *.* TO 'python_user'@'localhost' IDENTIFIED BY 'S3cR37_p@ss0WrD_r@d0|/|';

CREATE TABLE Users(
	id_user INT UNSIGNED AUTO_INCREMENT PRIMARY KEY
); 

CREATE TABLE Movies(
	id_movie INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(32) NOT NULL,
	image VARCHAR(32) NOT NULL,
	year YEAR,
	genres VARCHAR(128) NOT NULL
); 

CREATE TABLE Ratings(
	id_user INT UNSIGNED,
	id_movie INT UNSIGNED,
	rating TINYINT,
	time, TIMESTAMP,
	PRIMARY KEY(id_user, id_movie),
	FOREIGN KEY (id_user) REFERENCES Users(id_user) ON DELETE CASCADE,
	FOREIGN KEY (id_movie) REFERENCES Movies(id_movie) ON DELETE CASCADE
); 

CREATE TABLE Recommendations(
	id_movie INT UNSIGNED,
	id_recom INT UNSIGNED,
	position INT UNSIGNED,
	PRIMARY KEY(id_movie, id_recom),
	FOREIGN KEY (id_movie) REFERENCES Movies(id_movie) ON DELETE CASCADE,
	FOREIGN KEY (id_recom) REFERENCES Movies(id_movie) ON DELETE CASCADE
); 






