CREATE TABLE `summoner` (
  `id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `profile_icon_id` int(11) NOT NULL,
  `summoner_level` bigint(20) NOT NULL,
  `revision_date` bigint(20) NOT NULL,
  `update_date` bigint(20) NOT NULL,
  PRIMARY KEY (`id`,`account_id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `accountId_UNIQUE` (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;




CREATE TABLE `game_match` (
  `account_id` bigint(20) NOT NULL,
  `game_id` bigint(20) NOT NULL,
  `champion` int(11) NOT NULL,
  `lane` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `platform_id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `season` int(11) NOT NULL,
  `queue` int(11) NOT NULL,
  `role` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `match_timestamp` bigint(20) NOT NULL,
  PRIMARY KEY (`account_id`,`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `game` (
  `game_id` BIGINT(20) NOT NULL,
  `game_version` VARCHAR(45) NOT NULL,
  `platform_id` VARCHAR(45) NOT NULL,
  `game_mode` VARCHAR(45) NOT NULL,
  `map_id` INT NOT NULL,
  `game_type` VARCHAR(45) NOT NULL,
  `game_duration` BIGINT(20) NOT NULL,
  `game_creation` BIGINT(20) NOT NULL,
  PRIMARY KEY (`game_id`));

CREATE TABLE `game_participant` (
  `game_id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `summoner_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `participant_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `win` tinyint(4) NOT NULL,
  `champion_id` int(11) NOT NULL,
  `spell1_id` int(11) DEFAULT NULL,
  `spell2_id` int(11) DEFAULT NULL,
  `kills` int(11) NOT NULL,
  `deaths` int(11) NOT NULL,
  `assists` int(11) NOT NULL,
  `wardsKilled` int(11) NOT NULL,
  `wardsPlaced` int(11) NOT NULL,
  `sightWardsBoughtInGame` int(11) NOT NULL,
  `visionScore` int(11) NOT NULL,
  `timeCCingOthers` bigint(20) NOT NULL,
  `item0` int(11) DEFAULT NULL,
  `item1` int(11) DEFAULT NULL,
  `item2` int(11) DEFAULT NULL,
  `item3` int(11) DEFAULT NULL,
  `item4` int(11) DEFAULT NULL,
  `item5` int(11) DEFAULT NULL,
  `item6` int(11) DEFAULT NULL,
  PRIMARY KEY (`game_id`,`account_id`),
  KEY `ID_GAME_ID` (`game_id`),
  KEY `ID_ACCOUNT_ID` (`account_id`),
  CONSTRAINT `FK_GAME_ID` FOREIGN KEY (`game_id`) REFERENCES `game` (`game_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `champion_code` (
  `champion_id` int(11) NOT NULL,
  `title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `key` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`champion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `item_code` (
  `item_id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `plaintext` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `league` (
  `league_id` VARCHAR(100) NOT NULL,
  `tier` VARCHAR(50) NOT NULL,
  `queue` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`league_id`));

CREATE TABLE `league_item` (
  `league_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `player_or_team_id` bigint(20) NOT NULL,
  `player_or_team_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `league_points` int(11) NOT NULL,
  `rank` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `wins` int(11) NOT NULL,
  `losses` int(11) NOT NULL,
  `hot_streak` tinyint(4) NOT NULL,
  `veteran` tinyint(4) NOT NULL,
  `fresh_blood` tinyint(4) NOT NULL,
  `inactive` tinyint(4) NOT NULL,
  PRIMARY KEY (`league_id`,`player_or_team_id`),
  UNIQUE KEY `player_or_team_id_UNIQUE` (`player_or_team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `static_data` (
  `version` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `locale` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `data` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`version`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



