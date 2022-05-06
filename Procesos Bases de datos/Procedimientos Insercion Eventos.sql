USE Iglesia;

/*Insertar Eventos:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarEvento //
CREATE PROCEDURE InsertarEvento(eNombre VARCHAR(45), eFecha DATE, eHora TIME, eLugar VARCHAR(45))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    SELECT MAX(id) INTO IDNum FROM Evento;
    SET IDNum = IDNum +1;
    IF NOT EXISTS (SELECT * FROM Evento WHERE Nombre = eNombre) THEN
		IF NOT EXISTS (SELECT * FROM Evento WHERE Fecha = eFecha AND Hora = eHora AND Lugar = eLugar) THEN
			INSERT INTO Evento(id, Nombre, Fecha, Hora, Lugar) VALUES (IDNum, eNombre, eFecha, eHora, eLugar);
		END IF;
	END IF;
END; //
delimiter ;

/*Insertar Asistencia de Adolescentes:*/
delimiter //
DROP PROCEDURE IF EXISTS InsertarAsistenciaA //
CREATE PROCEDURE InsertarAsistenciaA(aNombre VARCHAR(45), eNombre VARCHAR(45))
BEGIN
	DECLARE IDNum INT DEFAULT 0;
    DECLARE IDAd INT DEFAULT 0;
    IF EXISTS (SELECT * FROM Adolescente WHERE Adolescente.nombre = aNombre) THEN
		SELECT id INTO IDNum FROM Adolescente WHERE Adolescente.nombre = aNombre;
        IF EXISTS (SELECT * FROM Evento WHERE Evento.nombre = eNombre) THEN
			SELECT id INTO IDAd FROM Evento WHERE Evento.nombre = eNombre;
            IF NOT EXISTS (SELECT * FROM asistenciaadolescente WHERE evento_id = IDNum AND adolescente_id = IDAd) THEN
				INSERT INTO asistenciaadolescente(evento_id,adolescente_id) VALUES (IDNum, IDAd);
			END IF;
		END IF;
	END IF;
END; //
delimiter ;