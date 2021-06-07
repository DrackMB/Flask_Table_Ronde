-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 30 mars 2021 à 16:39
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `table_ronde`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `id_admin` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `chevalier`
--

DROP TABLE IF EXISTS `chevalier`;
CREATE TABLE IF NOT EXISTS `chevalier` (
  `id_chevalier` int(11) NOT NULL AUTO_INCREMENT,
  `titre_chev` varchar(255) NOT NULL,
  `nom_chev` varchar(255) NOT NULL,
  `blason` varchar(255) NOT NULL,
  `reputation` varchar(255) NOT NULL,
  `id_quete` int(10) NOT NULL,
  `id_exploits` int(11) NOT NULL,
  `id_etat` int(11) NOT NULL,
  PRIMARY KEY (`id_chevalier`),
  KEY `fk_id_quete` (`id_quete`),
  KEY `fk_id_exploit` (`id_exploits`),
  KEY `fk_id_etat` (`id_etat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `etats`
--

DROP TABLE IF EXISTS `etats`;
CREATE TABLE IF NOT EXISTS `etats` (
  `id_etat` int(11) NOT NULL AUTO_INCREMENT,
  `Libelle` varchar(255) NOT NULL,
  PRIMARY KEY (`id_etat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `exploit`
--

DROP TABLE IF EXISTS `exploit`;
CREATE TABLE IF NOT EXISTS `exploit` (
  `id_exploit` int(11) NOT NULL AUTO_INCREMENT,
  `nom_ex` varchar(255) NOT NULL,
  `id_importance` int(11) NOT NULL,
  PRIMARY KEY (`id_exploit`),
  KEY `fk_id_importance` (`id_importance`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `importance`
--

DROP TABLE IF EXISTS `importance`;
CREATE TABLE IF NOT EXISTS `importance` (
  `id_importance` int(11) NOT NULL AUTO_INCREMENT,
  `libelle` varchar(255) NOT NULL,
  PRIMARY KEY (`id_importance`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `quete`
--

DROP TABLE IF EXISTS `quete`;
CREATE TABLE IF NOT EXISTS `quete` (
  `id_quete` int(11) NOT NULL AUTO_INCREMENT,
  `nom_quete` varchar(255) NOT NULL,
  `but` varchar(255) NOT NULL,
  `lieux` varchar(255) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id_quete`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `chevalier`
--
ALTER TABLE `chevalier`
  ADD CONSTRAINT `fk_id_etat` FOREIGN KEY (`id_etat`) REFERENCES `etats` (`id_etat`),
  ADD CONSTRAINT `fk_id_exploit` FOREIGN KEY (`id_exploits`) REFERENCES `exploit` (`id_exploit`),
  ADD CONSTRAINT `fk_id_quete` FOREIGN KEY (`id_quete`) REFERENCES `quete` (`id_quete`);

--
-- Contraintes pour la table `exploit`
--
ALTER TABLE `exploit`
  ADD CONSTRAINT `fk_id_chevalier` FOREIGN KEY (`id_chevalier`) REFERENCES `chevalier` (`id_chevalier`),
  ADD CONSTRAINT `fk_id_importance` FOREIGN KEY (`id_importance`) REFERENCES `importance` (`id_importance`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
