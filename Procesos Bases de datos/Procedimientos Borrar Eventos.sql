USE Iglesia;

delimiter //
DROP PROCEDURE IF EXISTS BorrarEvento //
CREATE PROCEDURE BorrarEvento(eNombre VARCHAR(45))
BEGIN
    DECLARE IDNum INT DEFAULT 0;
    SELECT id INTO IDNum FROM Evento WHERE Evento.Nombre = eNombre;
    DELETE FROM AsistenciaAdolescente WHERE AsistenciaAdolescente.Evento_id = IDNum;
    DELETE FROM AsistenciaColaborador WHERE AsistenciaColaborador.Evento_id = IDNum;
    DELETE FROM Evento WHERE Evento.id = IDNum;
END; //
delimiter ;

call BorrarEvento('JEJEJE');