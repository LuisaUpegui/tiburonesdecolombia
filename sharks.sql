-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema shark
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shark
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shark` DEFAULT CHARACTER SET utf8 ;
USE `shark` ;

-- -----------------------------------------------------
-- Table `shark`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shark`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `foto` VARCHAR(150) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(250) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `shark`.`magazines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shark`.`magazines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `nombre_comun` VARCHAR(45) NULL DEFAULT NULL,
  `habitos` VARCHAR(45) NULL DEFAULT NULL,
  `distribucion_col` VARCHAR(205) NULL DEFAULT NULL,
  `imagen` VARCHAR(140) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_magazines_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_magazines_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `shark`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB
AUTO_INCREMENT = 34
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `shark`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shark`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `magazine_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_magazines_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_magazines_has_users_magazines1_idx` (`magazine_id` ASC) VISIBLE,
  CONSTRAINT `fk_magazines_has_users_magazines1`
    FOREIGN KEY (`magazine_id`)
    REFERENCES `shark`.`magazines` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_magazines_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `shark`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 44
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
