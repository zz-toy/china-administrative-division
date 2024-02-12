SET FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE IF NOT EXISTS `govstat` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE govstat;

DROP TABLE IF EXISTS `province` ;
CREATE TABLE `province` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '省名称',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '省级代码',
  `full_code` varchar(20) NOT NULL DEFAULT '' COMMENT '统计用区划代码',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '被抓取的url',
  `child_url` varchar(200) NOT NULL DEFAULT '' COMMENT '指向的子url',
  `is_municipality` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是不是直辖市:1-是;0-否',
  `creator` varchar(32) NOT NULL DEFAULT '' COMMENT '创建者',
  `updater` varchar(32) NOT NULL DEFAULT '' COMMENT '更新者',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `data_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='省份表';

DROP TABLE IF EXISTS `city` ;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '城市名称',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '地级代码',
  `full_code` varchar(20) NOT NULL DEFAULT '' COMMENT '统计用区划代码',
  `province_id` int(11) NOT NULL DEFAULT '0' COMMENT 'province表id字段',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '被抓取的url',
  `child_url` varchar(200) NOT NULL DEFAULT '' COMMENT '指向的子url',
  `creator` varchar(32) NOT NULL DEFAULT '' COMMENT '创建者',
  `updater` varchar(32) NOT NULL DEFAULT '' COMMENT '更新者',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `data_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='城市表';

DROP TABLE IF EXISTS `county` ;
CREATE TABLE `county` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '县名称',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '县级代码',
  `full_code` varchar(20) NOT NULL DEFAULT '' COMMENT '统计用区划代码',
  `province_id` int(11) NOT NULL DEFAULT '0' COMMENT 'province表id字段',
  `city_id` int(11) NOT NULL DEFAULT '0' COMMENT 'city表id字段',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '被抓取的url',
  `child_url` varchar(200) NOT NULL DEFAULT '' COMMENT '指向的子url',
  `creator` varchar(32) NOT NULL DEFAULT '' COMMENT '创建者',
  `updater` varchar(32) NOT NULL DEFAULT '' COMMENT '更新者',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `data_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='县城表';

DROP TABLE IF EXISTS `town` ;
CREATE TABLE `town` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '乡镇名称',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '乡级代码',
  `full_code` varchar(20) NOT NULL DEFAULT '' COMMENT '统计用区划代码',
  `province_id` int(11) NOT NULL DEFAULT '0' COMMENT 'province表id字段',
  `city_id` int(11) NOT NULL DEFAULT '0' COMMENT 'city表id字段',
  `county_id` int(11) NOT NULL DEFAULT '0' COMMENT 'county表id字段',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '被抓取的url',
  `child_url` varchar(200) NOT NULL DEFAULT '' COMMENT '指向的子url',
  `creator` varchar(32) NOT NULL DEFAULT '' COMMENT '创建者',
  `updater` varchar(32) NOT NULL DEFAULT '' COMMENT '更新者',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `data_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='乡镇表';

DROP TABLE IF EXISTS `village` ;
CREATE TABLE `village` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '村庄名称',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '村级代码',
  `full_code` varchar(20) NOT NULL DEFAULT '' COMMENT '统计用区划代码',
  `classify_code` varchar(4) NOT NULL DEFAULT '' COMMENT '城乡分类码',
  `province_id` int(11) NOT NULL DEFAULT '0' COMMENT 'province表id字段',
  `city_id` int(11) NOT NULL DEFAULT '0' COMMENT 'city表id字段',
  `county_id` int(11) NOT NULL DEFAULT '0' COMMENT 'county表id字段',
  `town_id` int(11) NOT NULL DEFAULT '0' COMMENT 'town表id字段',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '被抓取的url',
  `creator` varchar(32) NOT NULL DEFAULT '' COMMENT '创建者',
  `updater` varchar(32) NOT NULL DEFAULT '' COMMENT '更新者',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `data_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='村庄表';


SET FOREIGN_KEY_CHECKS = 1;

TRUNCATE TABLE `province` ;
TRUNCATE TABLE `city` ;
TRUNCATE TABLE `county` ;
TRUNCATE TABLE `town` ;
TRUNCATE TABLE `village` ;