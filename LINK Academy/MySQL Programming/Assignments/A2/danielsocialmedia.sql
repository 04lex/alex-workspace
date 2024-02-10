-- tabel
CREATE TABLE IF NOT EXISTS Utilizator (
	UserID INT PRIMARY KEY,
    Prenume VARCHAR(50),
    Nume VARCHAR(50),
    DataNasterii DATE,
    LoculNasterii VARCHAR(100),
    Email VARCHAR(100),
    Username VARCHAR(50),
    CV TEXT,
    Fotografie BLOB
    );
    
CREATE TABLE IF NOT EXISTS Stare (
	StatusID INT PRIMARY KEY,
    Titlu VARCHAR(255),
    Continut TEXT,
    DataPublicare DATETIME,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES Utilizator(UserID)
);

CREATE TABLE IF NOT EXISTS Prietenie (
	PrietenieID INT PRIMARY KEY,
    Utilizator1ID INT,
    Utilizator2ID INT,
    DataPrietenie DATETIME,
    StarePrietenie ENUM('InAsteptare', 'Acceptat', 'Respins'),
    FOREIGN KEY (Utilizator1ID) REFERENCES Utilizator(UserID),
    FOREIGN KEY (Utilizator2ID) REFERENCES Utilizator(UserID)
);

-- index
ALTER TABLE Utilizator ADD INDEX idx_email (Email);
ALTER TABLE Stare ADD INDEX idx_user_id (UserID);
ALTER TABLE Prietenie ADD INDEX idx_utilizator1_id (Utilizator1ID), ADD INDEX idx_utilizator2_id (Utilizator2ID);

-- txt index
ALTER TABLE Stare ADD FULLTEXT INDEX idx_continut (Continut);

-- view
CREATE VIEW VizualizareUtilizator AS
SELECT UserID, Prenume, Nume, DataNasterii, LoculNasterii
FROM Utilizator;

-- proceduri
DELIMITER //
CREATE PROCEDURE AdaugareUtilizator(
	IN p_Prenume VARCHAR(50),
    IN p_Nume VARCHAR(50),
    IN p_DataNasterii DATE,
    IN p_LoculNasterii VARCHAR(100),
    IN p_Email VARCHAR(100),
    IN p_Username VARCHAR(50),
    IN p_CV TEXT,
    IN p_Fotografie BLOB
)
BEGIN
	INSERT INTO Utilizator (Prenume, Nume, DataNasterii, LoculNasterii, Email, Username, CV, Fotografie)
    VALUES (p_Prenume, p_Nume, p_DataNasterii, p_LoculNasterii, p_Email, p_Username, p_CV, p_Fotografie);
END //

CREATE PROCEDURE ModificareUtilizator(
	IN p_UserID INT,
    IN p_Prenume VARCHAR(50),
    IN p_Nume VARCHAR(50),
    IN p_DataNasterii DATE,
    IN p_LoculNasterii VARCHAR(100)
)

BEGIN
	UPDATE Utilizator
    SET Prenume = p_Prenume, Nume = p_Nume, DataNasterii = p_DataNasterii, LoculNasterii = p_LoculNasterii
    WHERE UserID = p_UserID;
END //

CREATE PROCEDURE StergereUtilizator(IN p_UserID INT)
BEGIN
	DELETE FROM Utilizator WHERE UserID = p_UserID;
END //

-- lista prieteni
CREATE FUNCTION NumarPrieteni(p_UserID INT) RETURNS INT 
BEGIN
	DECLARE total_prieteni INT;
    SELECT COUNT(*) INTO total_prieteni
    FROM Prietenie
    WHERE (Utilizator1ID = p_UserID OR Utilizator2ID = p_UserID) AND StarePrietenie = 'Acceptat';
END //

DELIMITER ;


    