USE Iglesia;

/*Insertar Colaborador:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarColab //
CREATE PROCEDURE InsertarColab(cNombre VARCHAR(45), cGenero VARCHAR(15), cNacimiento DATE,rango varchar(15))
BEGIN
	DECLARE IDrang INT DEFAULT 0;
	if(rango='Ministro') then
		Set IDrang=1;
	end if;
    if(rango='Lider') then
		Set IDrang=2;
	end if;
    if(rango='Teacher') then
		Set IDrang=3;
	end if;
    IF  NOT EXISTS (SELECT * FROM Colaborador WHERE Nombre = cNombre AND FechaNacimiento = cNacimiento) THEN
		INSERT INTO colaborador(FechaNacimiento, Nombre, Genero, Rango_id) VALUES (cNacimiento, cNombre, cGenero,IDrang);
	END IF;
END; //

/*Insertar Telefonos de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarTC //
CREATE PROCEDURE InsertarTC(cNombre VARCHAR(45), cTelefono VARCHAR(12))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Telefono;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM Colaborador WHERE Colaborador.nombre = cNombre) THEN
		SELECT id INTO IDAd FROM Colaborador WHERE Colaborador.nombre = cNombre;
        IF NOT EXISTS (SELECT * FROM Telefono WHERE Telefono = cTelefono AND Colaborador_id = IDAd) THEN
			INSERT INTO Telefono(id, Telefono, Colaborador_id) VALUES (IDNum, cTelefono, IDAd);
		END IF;
	END IF;
END; //
delimiter ;

delimiter ;
/*Insertar Informacion de Emergencia de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarIEC //
CREATE PROCEDURE InsertarIEC(aNombre VARCHAR(45), aSangre VARCHAR(5), aEncargado VARCHAR(45))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM InfoEmergencia;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM colaborador WHERE nombre = aNombre) THEN
		SELECT id INTO IDAd FROM colaborador WHERE nombre = aNombre;
        IF NOT EXISTS (SELECT * FROM InfoEmergencia WHERE Colaborador_id = IDAd) THEN
			INSERT INTO InfoEmergencia(id, TipoSangre, Encargado, Colaborador_id) VALUES (IDNum, aSangre, aEncargado, IDAd);
		END IF;
	END IF;
END; //
delimiter ;

/*Insertar Telefono de Informacion de Emergencia de Colaboradores:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarTIEC //
CREATE PROCEDURE InsertarTIEC(aNombre VARCHAR(45), aTelefono VARCHAR(12))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Telefono;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM colaborador WHERE colaborador.Nombre = aNombre) THEN
		SELECT id INTO IDAd FROM colaborador WHERE colaborador.Nombre = aNombre;
        IF EXISTS (SELECT * FROM InfoEmergencia WHERE InfoEmergencia.Colaborador_id = IDAd) THEN
			SELECT id INTO IDAd FROM InfoEmergencia WHERE InfoEmergencia.Colaborador_id = IDAd;
            IF NOT EXISTS (SELECT * FROM Telefono WHERE Telefono = aTelefono AND InfoEmergencia_id = IDAd) THEN
				INSERT INTO Telefono(id, Telefono, InfoEmergencia_id) VALUES (IDNum, aTelefono, IDAd);
			END IF;
		END IF;
	END IF;
END; //
delimiter ;
/*Insertar Alergia de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarAC //
CREATE PROCEDURE InsertarAC(aNombre VARCHAR(45), aDetalle VARCHAR(100))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Alergia;
    SET IDNum = IDNum +1;
    IF EXISTS (SELECT * FROM colaborador WHERE nombre = aNombre) THEN
		SELECT id INTO IDAd FROM colaborador WHERE nombre = aNombre;
        IF EXISTS (SELECT * FROM InfoEmergencia WHERE InfoEmergencia.Colaborador_id = IDAd) THEN
			SELECT id INTO IDAd FROM InfoEmergencia WHERE InfoEmergencia.Colaborador_id = IDAd;
            IF NOT EXISTS (SELECT * FROM Alergia WHERE Detalle = aDetalle AND InfoEmergencia_id = IDAd) THEN
				INSERT INTO Alergia(id, Detalle, InfoEmergencia_id) VALUES (IDNum, aDetalle, IDAd);
			END IF;
		END IF;
	END IF;
END; //
delimiter ;

/*Borrar Colaborador:*/
delimiter //
DROP PROCEDURE IF EXISTS BorrarColaborador //
CREATE PROCEDURE BorrarColaborador(cNombre VARCHAR(45))
BEGIN
    DECLARE IDNum INT DEFAULT 0;
    SELECT id INTO IDNum FROM Colaborador WHERE Colaborador.Nombre = cNombre;
    DELETE FROM Telefono WHERE Telefono.Colaborador_id = IDNum;
    DELETE FROM AsistenciaColaborador WHERE AsistenciaColaborador.Colaborador_id = IDNum;
    SELECT id INTO IDNum FROM InfoEmergencia WHERE InfoEmergencia.Colaborador_id = IDNum;
    DELETE FROM Telefono WHERE Telefono.InfoEmergencia_id = IDNum;
    DELETE FROM Alergia WHERE Alergia.InfoEmergencia_id = IDNum;
    DELETE FROM InfoEmergencia WHERE InfoEmergencia.id = IDNum;
    SELECT id INTO IDNum FROM Colaborador WHERE Colaborador.Nombre = cNombre;
    DELETE FROM Colaborador WHERE Colaborador.id = IDNum;
END; //
delimiter ;