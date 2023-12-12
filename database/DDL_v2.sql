-- #################################################################################
-- MySQL Dump of Project Schema with Sample Data
-- #################################################################################
-- Keifer Snedeker, Kevin Ngo
--
-- This file contains database initialization and sample data. The database
-- is composed of eight tables(3 look-up tables) and two intersection tables, see the 
-- submitted PDF for further description of each table and the significance of each relationship.
--
-- The sample data consists of six PowerSources mapped to four Substations
-- mapped to three Cities, with examples of how these M:N relationships handle 
-- single or many linkages. Each City is associated with a mandatory CityHQ, 
-- and one city has three LocalGenerators.
-- 
-- Further comments and documentation have been for additional clarity and 
-- description.
-- #################################################################################


SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- #################################################################################
-- Create the PowerSourcesTypes (Lookup table) with columns 
-- powerSourceTypeID (PK), type, and outputLoad.
-- #################################################################################
DROP TABLE IF EXISTS `PowerSourceTypes`;
CREATE TABLE `PowerSourceTypes` (
  `powerSourceTypeID` INT(11) NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(63) NOT NULL,
  `outputLoad` DECIMAL(11,2) NULL DEFAULT 0.0,
  PRIMARY KEY (`powerSourceTypeID`)
  );


-- #################################################################################
-- Create the PowerSources table with columns powerSourceID (PK), name, and 
-- powerSourceTypeID (FK)
-- #################################################################################
DROP TABLE IF EXISTS `PowerSources`;
CREATE TABLE `PowerSources` (
  `powerSourceID` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `powerSourceTypeID` INT(11),
  PRIMARY KEY (`powerSourceID`),
  CONSTRAINT `fk_PowerSources_PowerSourceTypes1`
    FOREIGN KEY (`powerSourceTypeID`)
    REFERENCES `PowerSourceTypes` (`powerSourceTypeID`)
    ON DELETE SET NULL
);


-- #################################################################################
-- Create the SubstationTypes (Lookup table) with columns 
-- substationTypeID (PK), size, and maxLoad.
-- #################################################################################
DROP TABLE IF EXISTS `SubstationTypes`;
CREATE TABLE `SubstationTypes` (
  `substationTypeID` INT NOT NULL AUTO_INCREMENT,
  `size` VARCHAR(63) NOT NULL,
  `maxLoad` DECIMAL(11,2) NOT NULL DEFAULT 0.0,
  PRIMARY KEY (`substationTypeID`)
);


-- #################################################################################
-- Create the Substations table with columns substationID(PK), name, currentLoad,
-- and substationTypeID (FK)
-- #################################################################################
DROP TABLE IF EXISTS `Substations`;
CREATE TABLE `Substations` (
  `substationID` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `currentLoad` DECIMAL(11,2) NOT NULL DEFAULT 0.0,
  `substationTypeID` INT,
  PRIMARY KEY (`substationID`),
  CONSTRAINT `fk_Substations_SubstationTypes1`
    FOREIGN KEY (`substationTypeID`)
    REFERENCES `SubstationTypes` (`substationTypeID`)
    ON DELETE SET NULL
);


-- #################################################################################
-- Create the Cities table with columns cityID (PK), name, population, energyDemand,
-- and currentLoad.
-- #################################################################################
DROP TABLE IF EXISTS `Cities`;
CREATE TABLE `Cities` (
  `cityID` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `population` INT(11) NOT NULL DEFAULT 0,
  `energyDemand` DECIMAL(11,2) NOT NULL DEFAULT 0.0,
  `currentLoad` DECIMAL(11,2) NOT NULL DEFAULT 0.0,
  PRIMARY KEY (`cityID`)
);

-- #################################################################################
-- Create the CityHQs table with columns hqID (PK), cityID (FK), and 
-- consumptionPolicy.
-- #################################################################################
DROP TABLE IF EXISTS `CityHQs`;
CREATE TABLE `CityHQs` (
  `hqID` INT(11) NOT NULL AUTO_INCREMENT,
  `cityID` INT(11) NULL,
  `consumptionPolicy` DECIMAL(3,2) NOT NULL DEFAULT 0.50,
  PRIMARY KEY (`hqID`),
  CONSTRAINT `fk_hq_cityID`
    FOREIGN KEY (`cityID`) REFERENCES `Cities` (`cityID`)
    ON DELETE CASCADE
);


-- #################################################################################
-- Create the LocalGeneratorTypes table with columns generatorTypeID (PK), type, and 
-- outputLoad.
-- #################################################################################
DROP TABLE IF EXISTS `LocalGeneratorTypes`;
CREATE TABLE `LocalGeneratorTypes` (
  `generatorTypeID` INT(11) NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(63) NOT NULL,
  `outputLoad` DECIMAL(11,2) NOT NULL,
  PRIMARY KEY (`generatorTypeID`)
);


-- #################################################################################
-- Create the LocalGenerators table with columns generatorID (PK), cityID(FK),
-- and generatorTypeID.
-- #################################################################################
DROP TABLE IF EXISTS `LocalGenerators`;
CREATE TABLE `LocalGenerators` (
  `generatorID` INT(11) NOT NULL AUTO_INCREMENT,
  `cityID` INT(11),
  `generatorTypeID` INT(11),
  PRIMARY KEY (`generatorID`),
  CONSTRAINT `fk_lg_cityID`
    FOREIGN KEY (`cityID`)
    REFERENCES `Cities` (`cityID`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_LocalGenerators_LocalGeneratorTypes1`
    FOREIGN KEY (`generatorTypeID`)
    REFERENCES `LocalGeneratorTypes` (`generatorTypeID`)
    ON DELETE SET NULL
);


-- #################################################################################
-- Create the PowerSourceSubstationLinks intersection table with columns
-- linkID (PK), powerSourceID (FK), and substationID (FK).
-- #################################################################################
DROP TABLE IF EXISTS `PowerSourceSubstationLinks`;
CREATE TABLE `PowerSourceSubstationLinks` (
  `linkID` INT(11) NOT NULL AUTO_INCREMENT,
  `powerSourceID` INT(11) NOT NULL,
  `substationID` INT(11) NOT NULL,
  PRIMARY KEY (`linkID`),
  CONSTRAINT `fk_psl_powerSourceID`
    FOREIGN KEY (`powerSourceID`) REFERENCES `PowerSources` (`powerSourceID`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_psl_substationID`
    FOREIGN KEY (`substationID`) REFERENCES `Substations` (`substationID`)
    ON DELETE CASCADE
);

-- #################################################################################
-- Create the CitySubstationLinks intersection table with columns
-- linkID (PK), substationID (FK), and cityID (FK).
-- #################################################################################
DROP TABLE IF EXISTS `CitySubstationLinks`;
CREATE TABLE `CitySubstationLinks` (
  `linkID` INT(11) NOT NULL AUTO_INCREMENT,
  `substationID` INT(11) NOT NULL,
  `cityID` INT(11) NOT NULL,
  PRIMARY KEY (`linkID`),
  CONSTRAINT `fk_csl_substationID`
    FOREIGN KEY (`substationID`) REFERENCES `Substations` (`substationID`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_csl_cityID`
    FOREIGN KEY (`cityID`) REFERENCES `Cities` (`cityID`)
    ON DELETE CASCADE
);



-- Insert sample data into PowerSourceTypes
-- Four PowerSourceTypes with varying types and outputLoads
INSERT INTO `PowerSourceTypes` (`type`, `outputLoad`) 
VALUES 
  ('Large Coal', 1200.00),
  ('Large Nuclear', 2000.00),
  ('Medium Hydro', 700.00),
  ('Medium Solar', 125.00);

-- Insert sample data into PowerSources
-- Six PowerSources entities with varying types and outputLoads
INSERT INTO `PowerSources` (`name`, `powerSourceTypeID`) 
VALUES
  ('LargeCoal1', (SELECT `powerSourceTypeID` FROM `PowerSourceTypes` WHERE `type` = 'Large Coal')),
  ('LargeCoal2', (SELECT `powerSourceTypeID` FROM `PowerSourceTypes` WHERE `type` = 'Large Coal')),
  ('LargeNuclear1', (SELECT `powerSourceTypeID` FROM `PowerSourceTypes` WHERE `type` = 'Large Nuclear')),
  ('MediumHydro1', (SELECT `powerSourceTypeID` FROM `PowerSourceTypes` WHERE `type` = 'Medium Hydro')),
  ('MediumSolar1', (SELECT `powerSourceTypeID` FROM `PowerSourceTypes` WHERE `type` = 'Medium Solar')),
  ('MediumSolar2', (SELECT `powerSourceTypeID` FROM `PowerSourceTypes` WHERE `type` = 'Medium Solar'));

-- Insert sample data into SubstationTypes
INSERT INTO `SubstationTypes` (`substationTypeID`, `size`, `maxLoad`)
VALUES
    (1, 'Mega', 2500.00),
    (2, 'Medium', 1000.00),
    (3, 'Small', 500.00);

-- Insert sample data into Substations
INSERT INTO `Substations` (`name`, `currentLoad`, `substationTypeID`)
VALUES
  ('SnNgSub1', 2400, (SELECT `substationTypeID` FROM `SubstationTypes` WHERE `size` = 'Mega')),
  ('SnSub1', 2000, (SELECT `substationTypeID` FROM `SubstationTypes` WHERE `size` = 'Mega')),
  ('NgSub1', 700, (SELECT `substationTypeID` FROM `SubstationTypes` WHERE `size` = 'Medium')),
  ('DaSub1', 250, (SELECT `substationTypeID` FROM `SubstationTypes` WHERE `size` = 'Small'));


-- Insert sample data into Cities
INSERT INTO `Cities` (`name`, `population`, `energyDemand`, `currentLoad`)
VALUES
    ('Snedekeria', 3200000, 2922.37, 3200),
    ('Ngopolis', 2000000, 1826.48, 1900),
    ('Databaseburg', 400000, 365.30, 400);

-- Insert sample data into CityHQs
INSERT INTO `CityHQs` (`cityID`, `consumptionPolicy`)
VALUES
    ((SELECT `cityID` FROM `Cities` WHERE `name` = 'Snedekeria'), 0.50),
    ((SELECT `cityID` FROM `Cities` WHERE `name` = 'Ngopolis'), 0.50),
    ((SELECT `cityID` FROM `Cities` WHERE `name` = 'Databaseburg'), 0.50);

-- Insert sample data into LocalGeneratorTypes 
INSERT INTO `LocalGeneratorTypes` (`type`, `outputLoad`) VALUES ('Rooftop Solar', 50.00);

-- Insert sample data into LocalGenerators (Intersection Table)
INSERT INTO `LocalGenerators` (`cityID`, `generatorTypeID`)
VALUES
    (1, (SELECT `generatorTypeID` FROM `LocalGeneratorTypes` WHERE `type` = 'Rooftop Solar')),
    (2, (SELECT `generatorTypeID` FROM `LocalGeneratorTypes` WHERE `type` = 'Rooftop Solar')),
    (3, (SELECT `generatorTypeID` FROM `LocalGeneratorTypes` WHERE `type` = 'Rooftop Solar'));


-- Insert sample data into PowerSourceSubstationLinks (Intersection Table)
INSERT INTO `PowerSourceSubstationLinks` (`powerSourceID`, `substationID`)
VALUES
    ((SELECT `powerSourceID` FROM `PowerSources` WHERE `name` = 'LargeCoal1'), 1),
    ((SELECT `powerSourceID` FROM `PowerSources` WHERE `name` = 'LargeCoal2'), 1),
    ((SELECT `powerSourceID` FROM `PowerSources` WHERE `name` = 'LargeNuclear1'), 2),
    ((SELECT `powerSourceID` FROM `PowerSources` WHERE `name` = 'MediumHydro1'), 3),
    ((SELECT `powerSourceID` FROM `PowerSources` WHERE `name` = 'MediumSolar1'), 4),
    ((SELECT `powerSourceID` FROM `PowerSources` WHERE `name` = 'MediumSolar2'), 4);

-- Insert sample data into CitySubstationLinks (Intersection Table)
INSERT INTO `CitySubstationLinks` (`substationID`, `cityID`)
VALUES
    ((SELECT `substationID` FROM `Substations` WHERE `name` = 'SnNgSub1'), 1),
    ((SELECT `substationID` FROM `Substations` WHERE `name` = 'SnNgSub1'), 2),
    ((SELECT `substationID` FROM `Substations` WHERE `name` = 'SnSub1'), 1),
    ((SELECT `substationID` FROM `Substations` WHERE `name` = 'NgSub1'), 2),
    ((SELECT `substationID` FROM `Substations` WHERE `name` = 'DaSub1'), 3);


SET FOREIGN_KEY_CHECKS=1;
COMMIT;