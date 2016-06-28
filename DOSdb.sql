-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema DOSdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema DOSdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DOSdb` DEFAULT CHARACTER SET utf8 ;
USE `DOSdb` ;

-- -----------------------------------------------------
-- Table `DOSdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`users` (
  `id` INT NOT NULL,
  `firstname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `pw_hash` VARCHAR(500) NULL,
  `servicename` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `phone` VARCHAR(45) NULL,
  `user_level` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`addresses` (
  `id` INT NOT NULL,
  `address1` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `zipcode` INT NULL,
  `apartment` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`users_has_addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`users_has_addresses` (
  `users_id` INT NOT NULL,
  `addresses_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `addresses_id`),
  INDEX `fk_Users_has_Addresses_Addresses1_idx` (`addresses_id` ASC),
  INDEX `fk_Users_has_Addresses_Users_idx` (`users_id` ASC),
  CONSTRAINT `fk_Users_has_Addresses_Users`
    FOREIGN KEY (`users_id`)
    REFERENCES `DOSdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Addresses_Addresses1`
    FOREIGN KEY (`addresses_id`)
    REFERENCES `DOSdb`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`vendors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`vendors` (
  `id` INT NOT NULL,
  `description` VARCHAR(500) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Vendors_Users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_Vendors_Users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `DOSdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`contractors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`contractors` (
  `id` INT NOT NULL,
  `description` VARCHAR(500) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`),
  INDEX `fk_Contractors_Users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_Contractors_Users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `DOSdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`vendor_reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`vendor_reviews` (
  `id` INT NOT NULL,
  `overall` INT NULL,
  `payment` INT NULL,
  `polite` INT NULL,
  `accurate` INT NULL,
  `review` TEXT NULL,
  `vendors_id` INT NOT NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_vendor_reviews_Vendors1_idx` (`vendors_id` ASC),
  INDEX `fk_vendor_reviews_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_vendor_reviews_Vendors1`
    FOREIGN KEY (`vendors_id`)
    REFERENCES `DOSdb`.`vendors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vendor_reviews_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `DOSdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`contractor_reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`contractor_reviews` (
  `id` INT NOT NULL,
  `quality` INT NULL,
  `politeness` INT NULL,
  `timeliness` INT NULL,
  `skill` INT NULL,
  `review` TEXT NULL,
  `contractors_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`),
  INDEX `fk_Contractor_reviews_Contractors1_idx` (`contractors_id` ASC),
  INDEX `fk_contractor_reviews_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_Contractor_reviews_Contractors1`
    FOREIGN KEY (`contractors_id`)
    REFERENCES `DOSdb`.`contractors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contractor_reviews_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `DOSdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`skills` (
  `id` INT NOT NULL,
  `skill` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`services`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`services` (
  `id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `description` VARCHAR(500) NULL,
  `price` VARCHAR(45) NULL,
  `contractors_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_services_Contractors1_idx` (`contractors_id` ASC),
  CONSTRAINT `fk_services_Contractors1`
    FOREIGN KEY (`contractors_id`)
    REFERENCES `DOSdb`.`contractors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`jobs` (
  `id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `description` VARCHAR(500) NULL,
  `price` VARCHAR(45) NULL,
  `vendors_id` INT NOT NULL,
  `time` DATETIME NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Jobs_Vendors1_idx` (`vendors_id` ASC),
  CONSTRAINT `fk_Jobs_Vendors1`
    FOREIGN KEY (`vendors_id`)
    REFERENCES `DOSdb`.`vendors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`skills_has_services`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`skills_has_services` (
  `skills_id` INT NOT NULL,
  `services_id` INT NOT NULL,
  PRIMARY KEY (`skills_id`, `services_id`),
  INDEX `fk_Skills_has_services_services1_idx` (`services_id` ASC),
  INDEX `fk_Skills_has_services_Skills1_idx` (`skills_id` ASC),
  CONSTRAINT `fk_Skills_has_services_Skills1`
    FOREIGN KEY (`skills_id`)
    REFERENCES `DOSdb`.`skills` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Skills_has_services_services1`
    FOREIGN KEY (`services_id`)
    REFERENCES `DOSdb`.`services` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`skills_has_jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`skills_has_jobs` (
  `skills_id` INT NOT NULL,
  `jobs_id` INT NOT NULL,
  PRIMARY KEY (`skills_id`, `jobs_id`),
  INDEX `fk_Skills_has_Jobs_Jobs1_idx` (`jobs_id` ASC),
  INDEX `fk_Skills_has_Jobs_Skills1_idx` (`skills_id` ASC),
  CONSTRAINT `fk_Skills_has_Jobs_Skills1`
    FOREIGN KEY (`skills_id`)
    REFERENCES `DOSdb`.`skills` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Skills_has_Jobs_Jobs1`
    FOREIGN KEY (`jobs_id`)
    REFERENCES `DOSdb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`bids`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`bids` (
  `id` INT NOT NULL,
  `price` FLOAT NULL,
  `comment` VARCHAR(45) NULL,
  `users_id` INT NOT NULL,
  `jobs_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `users_id`, `jobs_id`),
  INDEX `fk_bids_Users1_idx` (`users_id` ASC),
  INDEX `fk_bids_Jobs1_idx` (`jobs_id` ASC),
  CONSTRAINT `fk_bids_Users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `DOSdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bids_Jobs1`
    FOREIGN KEY (`jobs_id`)
    REFERENCES `DOSdb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`jobs_has_addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`jobs_has_addresses` (
  `jobs_id` INT NOT NULL,
  `addresses_id` INT NOT NULL,
  PRIMARY KEY (`jobs_id`, `addresses_id`),
  INDEX `fk_Jobs_has_Addresses_Addresses1_idx` (`addresses_id` ASC),
  INDEX `fk_Jobs_has_Addresses_Jobs1_idx` (`jobs_id` ASC),
  CONSTRAINT `fk_Jobs_has_Addresses_Jobs1`
    FOREIGN KEY (`jobs_id`)
    REFERENCES `DOSdb`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Jobs_has_Addresses_Addresses1`
    FOREIGN KEY (`addresses_id`)
    REFERENCES `DOSdb`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DOSdb`.`skills_has_contractors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DOSdb`.`skills_has_contractors` (
  `skills_id` INT NOT NULL,
  `contractors_id` INT NOT NULL,
  PRIMARY KEY (`skills_id`, `contractors_id`),
  INDEX `fk_skills_has_contractors_contractors1_idx` (`contractors_id` ASC),
  INDEX `fk_skills_has_contractors_skills1_idx` (`skills_id` ASC),
  CONSTRAINT `fk_skills_has_contractors_skills1`
    FOREIGN KEY (`skills_id`)
    REFERENCES `DOSdb`.`skills` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_skills_has_contractors_contractors1`
    FOREIGN KEY (`contractors_id`)
    REFERENCES `DOSdb`.`contractors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
