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
  `game_id` bigint(20) NOT NULL,
  `game_version` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `season_id` int(11) NOT NULL,
  `platform_id` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `game_mode` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `map_id` int(11) NOT NULL,
  `game_type` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `game_duration` bigint(20) NOT NULL,
  `game_creation` bigint(20) NOT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `game_participant` (
  `game_id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `summoner_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `participant_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `win` tinyint(4) NOT NULL,
  `champion_id` int(11) NOT NULL,
  `champ_level` int(11) NOT NULL DEFAULT '1',
  `role` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lane` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `spell1_id` int(11) DEFAULT NULL,
  `spell2_id` int(11) DEFAULT NULL,
  `kills` int(11) NOT NULL,
  `deaths` int(11) NOT NULL,
  `assists` int(11) NOT NULL,
  PRIMARY KEY (`game_id`,`account_id`),
  KEY `ID_GAME_ID` (`game_id`),
  KEY `ID_ACCOUNT_ID` (`account_id`),
  CONSTRAINT `FK_GAME_PARTICIPANT` FOREIGN KEY (`game_id`) REFERENCES `game` (`game_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

CREATE TABLE `participant_perk` (
  `game_id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `perkPrimaryStyle` int(11) NOT NULL DEFAULT '0',
  `perkSubStyle` int(11) NOT NULL DEFAULT '0',
  `perk0` int(11) NOT NULL DEFAULT '0',
  `perk1` int(11) NOT NULL DEFAULT '0',
  `perk2` int(11) NOT NULL DEFAULT '0',
  `perk3` int(11) NOT NULL DEFAULT '0',
  `perk4` int(11) NOT NULL DEFAULT '0',
  `perk5` int(11) NOT NULL DEFAULT '0',
  `perk0Var1` int(11) NOT NULL DEFAULT '0',
  `perk0Var2` int(11) NOT NULL DEFAULT '0',
  `perk0Var3` int(11) NOT NULL DEFAULT '0',
  `perk1Var1` int(11) NOT NULL DEFAULT '0',
  `perk1Var2` int(11) NOT NULL DEFAULT '0',
  `perk1Var3` int(11) NOT NULL DEFAULT '0',
  `perk2Var1` int(11) NOT NULL DEFAULT '0',
  `perk2Var2` int(11) NOT NULL DEFAULT '0',
  `perk2Var3` int(11) NOT NULL DEFAULT '0',
  `perk3Var1` int(11) NOT NULL DEFAULT '0',
  `perk3Var2` int(11) NOT NULL DEFAULT '0',
  `perk3Var3` int(11) NOT NULL DEFAULT '0',
  `perk4Var1` int(11) NOT NULL DEFAULT '0',
  `perk4Var2` int(11) NOT NULL DEFAULT '0',
  `perk4Var3` int(11) NOT NULL DEFAULT '0',
  `perk5Var1` int(11) NOT NULL DEFAULT '0',
  `perk5Var2` int(11) NOT NULL DEFAULT '0',
  `perk5Var3` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`game_id`,`account_id`),
  CONSTRAINT `FK_PARTICIPANT_PERK` FOREIGN KEY (`game_id`, `account_id`) REFERENCES `game_participant` (`game_id`, `account_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



CREATE TABLE `participant_item` (
  `game_id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `item0` int(11) NOT NULL DEFAULT '0',
  `item1` int(11) NOT NULL DEFAULT '0',
  `item2` int(11) NOT NULL DEFAULT '0',
  `item3` int(11) NOT NULL DEFAULT '0',
  `item4` int(11) NOT NULL DEFAULT '0',
  `item5` int(11) NOT NULL DEFAULT '0',
  `item6` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`game_id`,`account_id`),
  CONSTRAINT `FK_PARTICIPANT_ITEM` FOREIGN KEY (`game_id`, `account_id`) REFERENCES `game_participant` (`game_id`, `account_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `game_statistics` (
  `game_id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `neutralMinionsKilledTeamJungle` int(11) DEFAULT NULL,
  `visionScore` int(11) DEFAULT NULL,
  `magicDamageDealtToChampions` int(11) DEFAULT NULL,
  `largestMultiKill` int(11) DEFAULT NULL,
  `totalTimeCrowdControlDealt` int(11) DEFAULT NULL,
  `longestTimeSpentLiving` int(11) DEFAULT NULL,
  `tripleKills` int(11) DEFAULT NULL,
  `neutralMinionsKilled` int(11) DEFAULT NULL,
  `damageDealtToTurrets` int(11) DEFAULT NULL,
  `physicalDamageDealtToChampions` int(11) DEFAULT NULL,
  `damageDealtToObjectives` int(11) DEFAULT NULL,
  `totalUnitsHealed` int(11) DEFAULT NULL,
  `totalDamageTaken` int(11) DEFAULT NULL,
  `wardsKilled` int(11) DEFAULT NULL,
  `largestCriticalStrike` int(11) DEFAULT NULL,
  `largestKillingSpree` int(11) DEFAULT NULL,
  `quadraKills` int(11) DEFAULT NULL,
  `magicDamageDealt` int(11) DEFAULT NULL,
  `firstBloodAssist` tinyint(4) DEFAULT NULL,
  `damageSelfMitigated` int(11) DEFAULT NULL,
  `magicalDamageTaken` int(11) DEFAULT NULL,
  `trueDamageTaken` int(11) DEFAULT NULL,
  `goldSpent` int(11) DEFAULT NULL,
  `trueDamageDealt` int(11) DEFAULT NULL,
  `physicalDamageDealt` int(11) DEFAULT NULL,
  `sightWardsBoughtInGame` int(11) DEFAULT NULL,
  `totalDamageDealtToChampions` int(11) DEFAULT NULL,
  `physicalDamageTaken` int(11) DEFAULT NULL,
  `totalDamageDealt` int(11) DEFAULT NULL,
  `neutralMinionsKilledEnemyJungle` int(11) DEFAULT NULL,
  `wardsPlaced` int(11) DEFAULT NULL,
  `turretKills` int(11) DEFAULT NULL,
  `firstBloodKill` tinyint(4) DEFAULT NULL,
  `trueDamageDealtToChampions` int(11) DEFAULT NULL,
  `goldEarned` int(11) DEFAULT NULL,
  `killingSprees` int(11) DEFAULT NULL,
  `unrealKills` int(11) DEFAULT NULL,
  `firstTowerAssist` tinyint(4) DEFAULT NULL,
  `firstTowerKill` tinyint(4) DEFAULT NULL,
  `doubleKills` int(11) DEFAULT NULL,
  `inhibitorKills` int(11) DEFAULT NULL,
  `visionWardsBoughtInGame` int(11) DEFAULT NULL,
  `totalHeal` int(11) DEFAULT NULL,
  `pentaKills` int(11) DEFAULT NULL,
  `totalMinionsKilled` int(11) DEFAULT NULL,
  `timeCCingOthers` int(11) DEFAULT NULL,
  PRIMARY KEY (`game_id`,`account_id`),
  CONSTRAINT `FK_PARTICIPANT_STATIS` FOREIGN KEY (`game_id`, `account_id`) REFERENCES `game_participant` (`game_id`, `account_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

