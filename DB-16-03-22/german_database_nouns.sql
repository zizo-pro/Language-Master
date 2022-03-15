-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: german_database
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `nouns`
--

DROP TABLE IF EXISTS `nouns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nouns` (
  `article` varchar(5) NOT NULL,
  `noun` varchar(50) NOT NULL,
  `meaning` varchar(50) NOT NULL,
  `type` varchar(15) NOT NULL,
  `plural` varchar(50) NOT NULL,
  `category` varchar(20) NOT NULL,
  `example` varchar(100) NOT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=332 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nouns`
--

LOCK TABLES `nouns` WRITE;
/*!40000 ALTER TABLE `nouns` DISABLE KEYS */;
INSERT INTO `nouns` VALUES ('Das','Zimmer','Room','Noun','Die zimmer','Real state','Wir hatten ein Zimmer im Hotel',2),('Das','Auto','Car','Noun','Die Autos','Transportation','Ich fahre mein Auto',3),('Das','Foto','Photo','Noun','Die fotos','Media','Wir hatten ein Foto',4),('Das','Brot','Bread','Noun','Die Brote','Food','Ich habe Brot gegessen',5),('Der','Kopf','Head','Noun','Die köpfe','Körperteile','Mein kopf tut weh',323),('Das','Ohr','Ear','Noun','Die ohren','Körperteile','Ich höre mit die ohren',324),('Der','Mund','Mouth','Noun','Die münder','Körperteile','Du isst mit dein mund',325),('Die','Nase','Nose','Noun','Die nasen','Körperteile','Ich rieche mit meiner nase',326),('Der','Zahn','Tooth','Noun','Die zähne','Körperteile','Es gibt zähne im mund',327),('Die','Zunge','Toungue','Noun','Die zungen','Körperteile','Zunge ist rot',328),('Der','Hals','Throat','Noun','Die hälse','Körperteile','Meine hals tut weh',329),('Das','Haar','Hair','Noun','Die haare','Körperteile','Ich habe gelbe haare',330),('Die','Lippe','Lip','Noun','Die lippen','Körperteile','Meine lippen sind rot',331);
/*!40000 ALTER TABLE `nouns` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-16  0:05:46
