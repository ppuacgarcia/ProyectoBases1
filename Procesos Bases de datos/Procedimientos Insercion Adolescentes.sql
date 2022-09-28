USE Iglesia;

/*Insertar Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarAdolescente //
CREATE PROCEDURE InsertarAdolescente(aNombre VARCHAR(45), aGenero VARCHAR(15), aNacimiento DATE)
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Adolescente;
    SET IDNum = IDNum +1;
    IF  NOT EXISTS (SELECT * FROM Adolescente WHERE Nombre = aNombre AND FechaNacimiento = aNacimiento) THEN
		INSERT INTO Adolescente(id, Nombre, Genero, FechaNacimiento) VALUES (IDNum, aNombre, aGenero, aNacimiento);
	END IF;
END; //
delimiter ;

/*Insertar Telefonos de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarTA //
CREATE PROCEDURE InsertarTA(aNombre VARCHAR(45), aTelefono VARCHAR(12))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Telefono;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM Adolescente WHERE Adolescente.nombre = aNombre) THEN
		SELECT id INTO IDAd FROM Adolescente WHERE Adolescente.nombre = aNombre;
        IF NOT EXISTS (SELECT * FROM Telefono WHERE Telefono = aTelefono AND Adolescente_id = IDAd) THEN
			INSERT INTO Telefono(id, Telefono, Adolescente_id) VALUES (IDNum, aTelefono, IDAd);
		END IF;
	END IF;
END; //
delimiter ;

/*Insertar Informacion de Emergencia de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarIEA //
CREATE PROCEDURE InsertarIEA(aNombre VARCHAR(45), aSangre VARCHAR(5), aEncargado VARCHAR(45))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM InfoEmergencia;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM Adolescente WHERE Adolescente.nombre = aNombre) THEN
		SELECT id INTO IDAd FROM Adolescente WHERE Adolescente.nombre = aNombre;
        IF NOT EXISTS (SELECT * FROM InfoEmergencia WHERE Adolescente_id = IDAd) THEN
			INSERT INTO InfoEmergencia(id, TipoSangre, Encargado, Adolescente_id) VALUES (IDNum, aSangre, aEncargado, IDAd);
		END IF;
	END IF;
END; //
delimiter ;

/*Insertar Telefono de Informacion de Emergencia de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarTIEA //
CREATE PROCEDURE InsertarTIEA(aNombre VARCHAR(45), aTelefono VARCHAR(12))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Telefono;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM Adolescente WHERE Adolescente.Nombre = aNombre) THEN
		SELECT id INTO IDAd FROM Adolescente WHERE Adolescente.Nombre = aNombre;
        IF EXISTS (SELECT * FROM InfoEmergencia WHERE InfoEmergencia.Adolescente_id = IDAd) THEN
			SELECT id INTO IDAd FROM InfoEmergencia WHERE InfoEmergencia.Adolescente_id = IDAd;
            IF NOT EXISTS (SELECT * FROM Telefono WHERE Telefono = aTelefono AND InfoEmergencia_id = IDAd) THEN
				INSERT INTO Telefono(id, Telefono, InfoEmergencia_id) VALUES (IDNum, aTelefono, IDAd);
			END IF;
		END IF;
	END IF;
END; //
delimiter ;

/*Insertar Alergia de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarAA //
CREATE PROCEDURE InsertarAA(aNombre VARCHAR(45), aDetalle VARCHAR(100))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Alergia;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM Adolescente WHERE Adolescente.nombre = aNombre) THEN
		SELECT id INTO IDAd FROM Adolescente WHERE Adolescente.nombre = aNombre;
        IF EXISTS (SELECT * FROM InfoEmergencia WHERE InfoEmergencia.Adolescente_id = IDAd) THEN
			SELECT id INTO IDAd FROM InfoEmergencia WHERE InfoEmergencia.Adolescente_id = IDAd;
            IF NOT EXISTS (SELECT * FROM Alergia WHERE Detalle = aDetalle AND InfoEmergencia_id = IDAd) THEN
				INSERT INTO Alergia(id, Detalle, InfoEmergencia_id) VALUES (IDNum, aDetalle, IDAd);
			END IF;
		END IF;
	END IF;
END; //
delimiter ;