-- MariaDB dump 10.19  Distrib 10.7.3-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: iglesia
-- ------------------------------------------------------
-- Server version	10.7.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adolescente`
--

DROP TABLE IF EXISTS `adolescente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adolescente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Genero` varchar(15) DEFAULT NULL,
  `FechaNacimiento` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adolescente`
--

LOCK TABLES `adolescente` WRITE;
/*!40000 ALTER TABLE `adolescente` DISABLE KEYS */;
INSERT INTO `adolescente` VALUES
(1,'pablo','Masculino','2022-05-05'),
(2,'hola','Masculino','2022-05-05'),
(3,'MUCHO','MASCULINO','2022-05-05'),
(4,'HOLAMUNDO','MASCULINO','2022-05-05'),
(5,'HOLA','MASCULINO','2022-09-26'),
(6,'PABLO','MASCULINO','2022-09-26'),
(7,'SAD','MASCULINO','2022-09-26'),
(8,'SDAS','MASCULINO','2022-09-26'),
(9,'DSADSA','MASCULINO','2022-09-26'),
(10,'SADSAD','MASCULINO','2022-09-26'),
(11,'DASDSA','MASCULINO','2022-09-26'),
(12,'DASD','MASCULINO','2022-09-26'),
(13,'DSAD','MASCULINO','2022-09-26'),
(14,'SDA','MASCULINO','2022-09-26'),
(15,'DASDAS','MASCULINO','2022-09-27'),
(16,'AAA','MASCULINO','2022-09-27'),
(17,'AAB','MASCULINO','2022-09-27'),
(18,'A','MASCULINO','2022-09-27'),
(19,'AA','MASCULINO','2022-09-27'),
(20,'DAS','MASCULINO','2022-09-27'),
(21,'SSSS','MASCULINO','2022-09-27'),
(22,'DSADA','MASCULINO','2022-09-27'),
(23,'z','MASCULINO','2022-09-27'),
(24,'zzz','MASCULINO','2022-09-27'),
(25,'zz','MASCULINO','2022-09-27'),
(26,'zzzzz','MASCULINO','2022-09-27');
/*!40000 ALTER TABLE `adolescente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alergia`
--

DROP TABLE IF EXISTS `alergia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alergia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Detalle` varchar(100) DEFAULT NULL,
  `InfoEmergencia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Alergia_InfoEmergencia1_idx` (`InfoEmergencia_id`),
  CONSTRAINT `fk_Alergia_InfoEmergencia1` FOREIGN KEY (`InfoEmergencia_id`) REFERENCES `infoemergencia` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alergia`
--

LOCK TABLES `alergia` WRITE;
/*!40000 ALTER TABLE `alergia` DISABLE KEYS */;
INSERT INTO `alergia` VALUES
(1,'si',1),
(2,'mani',2),
(3,'7',3),
(4,'SI',4),
(5,'SI',6),
(6,'siasd',7),
(7,'a',9);
/*!40000 ALTER TABLE `alergia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistenciaadolescente`
--

DROP TABLE IF EXISTS `asistenciaadolescente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistenciaadolescente` (
  `Evento_id` int(11) NOT NULL,
  `Adolescente_id` int(11) NOT NULL,
  PRIMARY KEY (`Evento_id`,`Adolescente_id`),
  KEY `fk_Evento_has_Adolescente_Adolescente1_idx` (`Adolescente_id`),
  KEY `fk_Evento_has_Adolescente_Evento1_idx` (`Evento_id`),
  CONSTRAINT `fk_Evento_has_Adolescente_Adolescente1` FOREIGN KEY (`Adolescente_id`) REFERENCES `adolescente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Evento_has_Adolescente_Evento1` FOREIGN KEY (`Evento_id`) REFERENCES `evento` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistenciaadolescente`
--

LOCK TABLES `asistenciaadolescente` WRITE;
/*!40000 ALTER TABLE `asistenciaadolescente` DISABLE KEYS */;
/*!40000 ALTER TABLE `asistenciaadolescente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistenciacolaborador`
--

DROP TABLE IF EXISTS `asistenciacolaborador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistenciacolaborador` (
  `Evento_id` int(11) NOT NULL,
  `Colaborador_id` int(11) NOT NULL,
  PRIMARY KEY (`Evento_id`,`Colaborador_id`),
  KEY `fk_Evento_has_Colaborador_Colaborador1_idx` (`Colaborador_id`),
  KEY `fk_Evento_has_Colaborador_Evento1_idx` (`Evento_id`),
  CONSTRAINT `fk_Evento_has_Colaborador_Colaborador1` FOREIGN KEY (`Colaborador_id`) REFERENCES `colaborador` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Evento_has_Colaborador_Evento1` FOREIGN KEY (`Evento_id`) REFERENCES `evento` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistenciacolaborador`
--

LOCK TABLES `asistenciacolaborador` WRITE;
/*!40000 ALTER TABLE `asistenciacolaborador` DISABLE KEYS */;
/*!40000 ALTER TABLE `asistenciacolaborador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaborador`
--

DROP TABLE IF EXISTS `colaborador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colaborador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FechaNacimiento` date DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Genero` varchar(15) DEFAULT NULL,
  `Rango_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Colaborador_Rango1_idx` (`Rango_id`),
  CONSTRAINT `fk_Colaborador_Rango1` FOREIGN KEY (`Rango_id`) REFERENCES `rango` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaborador`
--

LOCK TABLES `colaborador` WRITE;
/*!40000 ALTER TABLE `colaborador` DISABLE KEYS */;
INSERT INTO `colaborador` VALUES
(1,'2022-05-05','pablo','Masculino',3),
(2,'2022-05-05','pablodpg','Masculino',3),
(3,'2022-05-05','juanito','Masculino',3),
(4,'2022-05-05','holam','Masculino',3),
(5,'2022-05-06','pedro','Masculino',3),
(6,'2022-05-06','sdasdsdsad','Masculino',3),
(7,'2022-05-06','holamundooooo','Masculino',3),
(8,'2022-05-06','HOLAAAAAA','Masculino',3),
(9,'2022-05-06','pedrito','Masculino',3),
(11,'2022-09-27','dsad','Masculino',3);
/*!40000 ALTER TABLE `colaborador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evento`
--

DROP TABLE IF EXISTS `evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Hora` time DEFAULT NULL,
  `Lugar` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evento`
--

LOCK TABLES `evento` WRITE;
/*!40000 ALTER TABLE `evento` DISABLE KEYS */;
/*!40000 ALTER TABLE `evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infoemergencia`
--

DROP TABLE IF EXISTS `infoemergencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `infoemergencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `TipoSangre` varchar(5) DEFAULT NULL,
  `Encargado` varchar(45) DEFAULT NULL,
  `Colaborador_id` int(11) DEFAULT NULL,
  `Adolescente_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_InformacionEnmergenica_Colaborador1_idx` (`Colaborador_id`),
  KEY `fk_InformacionEnmergenica_Adolescente1_idx` (`Adolescente_id`),
  CONSTRAINT `fk_InformacionEnmergenica_Adolescente1` FOREIGN KEY (`Adolescente_id`) REFERENCES `adolescente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_InformacionEnmergenica_Colaborador1` FOREIGN KEY (`Colaborador_id`) REFERENCES `colaborador` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infoemergencia`
--

LOCK TABLES `infoemergencia` WRITE;
/*!40000 ALTER TABLE `infoemergencia` DISABLE KEYS */;
INSERT INTO `infoemergencia` VALUES
(1,'a+','pablop',NULL,1),
(2,'b+','pablo',NULL,2),
(3,'B-','GUSTO',NULL,3),
(4,'B-','COMO',NULL,4),
(5,'b-','si',7,NULL),
(6,'NO','SDASD',8,NULL),
(7,'b+','alex',9,NULL),
(8,'A+','SDASD',NULL,1),
(9,'a','sdas',11,NULL);
/*!40000 ALTER TABLE `infoemergencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rango`
--

DROP TABLE IF EXISTS `rango`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rango` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Rango` varchar(45) DEFAULT NULL,
  `Permiso` smallint(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rango`
--

LOCK TABLES `rango` WRITE;
/*!40000 ALTER TABLE `rango` DISABLE KEYS */;
INSERT INTO `rango` VALUES
(1,'Ministro',0),
(2,'Lider',0),
(3,'Teacher',0);
/*!40000 ALTER TABLE `rango` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telefono`
--

DROP TABLE IF EXISTS `telefono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `telefono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Telefono` varchar(12) DEFAULT NULL,
  `Colaborador_id` int(11) DEFAULT NULL,
  `Adolescente_id` int(11) DEFAULT NULL,
  `InfoEmergencia_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Telefono_Colaborador1_idx` (`Colaborador_id`),
  KEY `fk_Telefono_Adolescente1_idx` (`Adolescente_id`),
  KEY `fk_Telefono_InfoEmergencia1_idx` (`InfoEmergencia_id`),
  CONSTRAINT `fk_Telefono_Adolescente1` FOREIGN KEY (`Adolescente_id`) REFERENCES `adolescente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Telefono_Colaborador1` FOREIGN KEY (`Colaborador_id`) REFERENCES `colaborador` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Telefono_InfoEmergencia1` FOREIGN KEY (`InfoEmergencia_id`) REFERENCES `infoemergencia` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telefono`
--

LOCK TABLES `telefono` WRITE;
/*!40000 ALTER TABLE `telefono` DISABLE KEYS */;
INSERT INTO `telefono` VALUES
(1,'123456',NULL,1,NULL),
(2,'553',NULL,2,NULL),
(3,'213',NULL,1,NULL),
(4,'55113355',NULL,3,NULL),
(5,'5646',NULL,4,NULL),
(6,'7456',NULL,NULL,6),
(7,'655',NULL,NULL,7),
(8,'123',NULL,7,NULL),
(9,'213213',NULL,8,NULL),
(10,'214321',NULL,9,NULL),
(11,'21321',NULL,10,NULL),
(12,'2132',NULL,11,NULL),
(13,'213123',NULL,12,NULL),
(14,'1232sdad',NULL,13,NULL),
(15,'123',NULL,8,NULL),
(16,'2132',NULL,15,NULL),
(17,'21321',NULL,16,NULL),
(18,'231',NULL,17,NULL),
(19,'3213',NULL,18,NULL),
(20,'a',NULL,18,NULL),
(21,'132165',NULL,19,NULL),
(22,'5513',NULL,20,NULL),
(23,'21321',NULL,20,NULL),
(24,'12231',NULL,21,NULL),
(25,'42343',NULL,NULL,9),
(26,'213312',NULL,22,NULL),
(27,'3123',NULL,23,NULL),
(28,'123213',NULL,24,NULL),
(29,'zzz',NULL,24,NULL),
(30,'zzz',NULL,25,NULL),
(31,'21323',NULL,26,NULL);
/*!40000 ALTER TABLE `telefono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Clave` varchar(45) DEFAULT NULL,
  `Colaborador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_Usuario_Colaborador1_idx` (`Colaborador_id`),
  CONSTRAINT `fk_Usuario_Colaborador1` FOREIGN KEY (`Colaborador_id`) REFERENCES `colaborador` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-28  0:38:34
