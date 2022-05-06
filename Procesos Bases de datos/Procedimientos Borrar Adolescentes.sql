USE Iglesia;

delimiter //
DROP PROCEDURE IF EXISTS BorrarAdolescente //
CREATE PROCEDURE BorrarAdolescente(aNombre VARCHAR(45))
BEGIN
    DECLARE IDNum INT DEFAULT 0;
    SELECT id INTO IDNum FROM Adolescente WHERE Adolescente.Nombre = aNombre;
    DELETE FROM Telefono WHERE Telefono.Adolescente_id = IDNum;
    DELETE FROM AsistenciaAdolescente WHERE AsistenciaAdolescente.Adolescente_id = IDNum;
    SELECT id INTO IDNum FROM InfoEmergencia WHERE InfoEmergencia.Adolescente_id = IDNum;
    DELETE FROM Telefono WHERE Telefono.InfoEmergencia_id = IDNum;
    DELETE FROM Alergia WHERE Alergia.InfoEmergencia_id = IDNum;
    DELETE FROM InfoEmergencia WHERE InfoEmergencia.id = IDNum;
    SELECT id INTO IDNum FROM Adolescente WHERE Adolescente.Nombre = aNombre;
    DELETE FROM Adolescente WHERE Adolescente.id = IDNum;
END; //
delimiter ;
