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
delimiter ;
