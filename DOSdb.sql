-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: DOSdb
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address1` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `zipcode` int(11) DEFAULT NULL,
  `state` varchar(25) DEFAULT NULL,
  `apartment` varchar(45) DEFAULT NULL,
  `home` int(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (14,'4726 Armour Drive','Santa Clara',95054,NULL,'N/A',NULL,'2016-06-28 20:49:15','2016-06-28 20:49:15'),(15,'4726 Armour Drive','Santa Clara',95054,NULL,'N/A',NULL,NULL,NULL),(16,'4726 Armour Drive','Santa Clara',95054,NULL,'N/A',NULL,NULL,NULL),(17,'123 Test St.','San Francisco',95054,NULL,'N/A',NULL,NULL,NULL),(18,'123 Test St.','San Francisco',95054,NULL,'N/A',NULL,NULL,NULL),(19,'4726 Armour Drive','Santa Clara',95054,'CA','N/A',1,'2016-06-28 22:42:49','2016-06-28 22:42:49');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bids`
--

DROP TABLE IF EXISTS `bids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bids` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `comment` varchar(45) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`user_id`,`job_id`),
  KEY `fk_bids_Users1_idx` (`user_id`),
  KEY `fk_bids_Jobs1_idx` (`job_id`),
  CONSTRAINT `fk_bids_Jobs1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_bids_Users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bids`
--

LOCK TABLES `bids` WRITE;
/*!40000 ALTER TABLE `bids` DISABLE KEYS */;
/*!40000 ALTER TABLE `bids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contractor_reviews`
--

DROP TABLE IF EXISTS `contractor_reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contractor_reviews` (
  `id` int(11) NOT NULL,
  `quality` int(11) DEFAULT NULL,
  `politeness` int(11) DEFAULT NULL,
  `timeliness` int(11) DEFAULT NULL,
  `skill` int(11) DEFAULT NULL,
  `review` text,
  `contractor_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_Contractor_reviews_Contractors1_idx` (`contractor_id`),
  KEY `fk_contractor_reviews_users1_idx` (`user_id`),
  CONSTRAINT `fk_Contractor_reviews_Contractors1` FOREIGN KEY (`contractor_id`) REFERENCES `contractors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_contractor_reviews_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contractor_reviews`
--

LOCK TABLES `contractor_reviews` WRITE;
/*!40000 ALTER TABLE `contractor_reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `contractor_reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contractors`
--

DROP TABLE IF EXISTS `contractors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contractors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_Contractors_Users1_idx` (`user_id`),
  CONSTRAINT `fk_Contractors_Users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contractors`
--

LOCK TABLES `contractors` WRITE;
/*!40000 ALTER TABLE `contractors` DISABLE KEYS */;
/*!40000 ALTER TABLE `contractors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `accepted_id` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_has_addresses`
--

DROP TABLE IF EXISTS `jobs_has_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_has_addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`job_id`,`address_id`),
  KEY `fk_Jobs_has_Addresses_Addresses1_idx` (`address_id`),
  KEY `fk_Jobs_has_Addresses_Jobs1_idx` (`job_id`),
  CONSTRAINT `fk_Jobs_has_Addresses_Addresses1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Jobs_has_Addresses_Jobs1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_has_addresses`
--

LOCK TABLES `jobs_has_addresses` WRITE;
/*!40000 ALTER TABLE `jobs_has_addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_has_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `contractor_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_services_Contractors1_idx` (`contractor_id`),
  CONSTRAINT `fk_services_Contractors1` FOREIGN KEY (`contractor_id`) REFERENCES `contractors` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `skills` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `skill` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills_has_contractors`
--

DROP TABLE IF EXISTS `skills_has_contractors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `skills_has_contractors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `skill_id` int(11) NOT NULL,
  `contractor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`skill_id`,`contractor_id`),
  KEY `fk_skills_has_contractors_contractors1_idx` (`contractor_id`),
  KEY `fk_skills_has_contractors_skills1_idx` (`skill_id`),
  CONSTRAINT `fk_skills_has_contractors_contractors1` FOREIGN KEY (`contractor_id`) REFERENCES `contractors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_skills_has_contractors_skills1` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills_has_contractors`
--

LOCK TABLES `skills_has_contractors` WRITE;
/*!40000 ALTER TABLE `skills_has_contractors` DISABLE KEYS */;
/*!40000 ALTER TABLE `skills_has_contractors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills_has_jobs`
--

DROP TABLE IF EXISTS `skills_has_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `skills_has_jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `skill_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`skill_id`,`job_id`),
  KEY `fk_Skills_has_Jobs_Jobs1_idx` (`job_id`),
  KEY `fk_Skills_has_Jobs_Skills1_idx` (`skill_id`),
  CONSTRAINT `fk_Skills_has_Jobs_Jobs1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Skills_has_Jobs_Skills1` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills_has_jobs`
--

LOCK TABLES `skills_has_jobs` WRITE;
/*!40000 ALTER TABLE `skills_has_jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `skills_has_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills_has_services`
--

DROP TABLE IF EXISTS `skills_has_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `skills_has_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `skill_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`skill_id`,`service_id`),
  KEY `fk_Skills_has_services_services1_idx` (`service_id`),
  KEY `fk_Skills_has_services_Skills1_idx` (`skill_id`),
  CONSTRAINT `fk_Skills_has_services_services1` FOREIGN KEY (`service_id`) REFERENCES `services` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Skills_has_services_Skills1` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills_has_services`
--

LOCK TABLES `skills_has_services` WRITE;
/*!40000 ALTER TABLE `skills_has_services` DISABLE KEYS */;
/*!40000 ALTER TABLE `skills_has_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `pw_hash` varchar(500) DEFAULT NULL,
  `servicename` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `user_level` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (21,'Connor','Paull','email@email.com','$2b$12$dDEq3mTLHR3uuqBj1t5bZ.OMWd4QozFtN2IqLUL5I8Bn0wraNRED2',NULL,'2016-06-28 20:49:15','2016-06-28 20:49:15','9999999999','0'),(22,'User','Two','email@email.com','$2b$12$dghk9FlDKvSytcz7zOZchef1OAQL1INMb/F8VUdCxl5cMPf5PNd9y',NULL,'2016-06-28 21:01:01','2016-06-28 21:01:01','9999999999','0'),(23,'Connor','Paull','email@email.com','$2b$12$Ix6sYO0DkOfFnmAPHQ/08O0GSJNi.evBiPBQcAPm5tcZYF/ujM652',NULL,'2016-06-28 21:04:00','2016-06-28 21:04:00','9999999999','0'),(24,'Connor','Paull','cbpaull@gmail.com','$2b$12$J37t9CnXVBN4ju5Fb8utSuwjGD.Ha3ueivyUDSjyPb4B4pltJpX2O',NULL,'2016-06-28 21:21:38','2016-06-28 21:21:38','9999999999','0'),(25,'Ceebee','Paull','testbug@gmail.com','$2b$12$GA2ebyXyY.PmjM/8r4V.eurxS7Fao1.2njanvl.Dy2uXvLigN4Jha',NULL,'2016-06-28 22:28:34','2016-06-28 22:28:34','9999999999','0'),(26,'User','Bob','testbug@gmail.com','$2b$12$y.TcxPWy19diaqQQhQIVzuGzM9NA.0yLU.e/rj1jOdPzNxOVv9J4.',NULL,'2016-06-28 22:41:07','2016-06-28 22:41:07','9999999999','0'),(27,'User','Bob','testbug@gmail.com','$2b$12$1siN4seMTVwxH4TKo8Mwuuh1UojJctLR8II7XauB8Uh2EJfmviKKm',NULL,'2016-06-28 22:42:49','2016-06-28 22:42:49','9999999999','0');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_has_addresses`
--

DROP TABLE IF EXISTS `users_has_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_has_addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`user_id`,`address_id`),
  KEY `fk_Users_has_Addresses_Addresses1_idx` (`address_id`),
  KEY `fk_Users_has_Addresses_Users_idx` (`user_id`),
  CONSTRAINT `fk_Users_has_Addresses_Addresses1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Addresses_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_has_addresses`
--

LOCK TABLES `users_has_addresses` WRITE;
/*!40000 ALTER TABLE `users_has_addresses` DISABLE KEYS */;
INSERT INTO `users_has_addresses` VALUES (1,22,15),(2,23,16),(3,24,17),(4,25,18),(5,27,19);
/*!40000 ALTER TABLE `users_has_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor_reviews`
--

DROP TABLE IF EXISTS `vendor_reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendor_reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `overall` int(11) DEFAULT NULL,
  `payment` int(11) DEFAULT NULL,
  `polite` int(11) DEFAULT NULL,
  `accurate` int(11) DEFAULT NULL,
  `review` text,
  `vendor_id` int(11) NOT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `updated_at` varchar(45) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_vendor_reviews_Vendors1_idx` (`vendor_id`),
  KEY `fk_vendor_reviews_users1_idx` (`user_id`),
  CONSTRAINT `fk_vendor_reviews_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_vendor_reviews_Vendors1` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor_reviews`
--

LOCK TABLES `vendor_reviews` WRITE;
/*!40000 ALTER TABLE `vendor_reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendor_reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendors`
--

DROP TABLE IF EXISTS `vendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) DEFAULT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `updated_at` varchar(45) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Vendors_Users1_idx` (`user_id`),
  CONSTRAINT `fk_Vendors_Users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendors`
--

LOCK TABLES `vendors` WRITE;
/*!40000 ALTER TABLE `vendors` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-29  0:51:42
