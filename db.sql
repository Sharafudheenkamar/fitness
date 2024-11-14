/*
SQLyog Community v12.4.0 (64 bit)
MySQL - 8.0.31 : Database - fitnesspro
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fitnesspro` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `fitnesspro`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add category',7,'add_category'),
(26,'Can change category',7,'change_category'),
(27,'Can delete category',7,'delete_category'),
(28,'Can view category',7,'view_category'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add user',9,'add_user'),
(34,'Can change user',9,'change_user'),
(35,'Can delete user',9,'delete_user'),
(36,'Can view user',9,'view_user'),
(37,'Can add trainer',10,'add_trainer'),
(38,'Can change trainer',10,'change_trainer'),
(39,'Can delete trainer',10,'delete_trainer'),
(40,'Can view trainer',10,'view_trainer'),
(41,'Can add posture',11,'add_posture'),
(42,'Can change posture',11,'change_posture'),
(43,'Can delete posture',11,'delete_posture'),
(44,'Can view posture',11,'view_posture'),
(45,'Can add payment',12,'add_payment'),
(46,'Can change payment',12,'change_payment'),
(47,'Can delete payment',12,'delete_payment'),
(48,'Can view payment',12,'view_payment'),
(49,'Can add feedback',13,'add_feedback'),
(50,'Can change feedback',13,'change_feedback'),
(51,'Can delete feedback',13,'delete_feedback'),
(52,'Can view feedback',13,'view_feedback'),
(53,'Can add diet',14,'add_diet'),
(54,'Can change diet',14,'change_diet'),
(55,'Can delete diet',14,'delete_diet'),
(56,'Can view diet',14,'view_diet'),
(57,'Can add complaint',15,'add_complaint'),
(58,'Can change complaint',15,'change_complaint'),
(59,'Can delete complaint',15,'delete_complaint'),
(60,'Can view complaint',15,'view_complaint'),
(61,'Can add chat',16,'add_chat'),
(62,'Can change chat',16,'change_chat'),
(63,'Can delete chat',16,'delete_chat'),
(64,'Can view chat',16,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'myapp','category'),
(8,'myapp','login'),
(9,'myapp','user'),
(10,'myapp','trainer'),
(11,'myapp','posture'),
(12,'myapp','payment'),
(13,'myapp','feedback'),
(14,'myapp','diet'),
(15,'myapp','complaint'),
(16,'myapp','chat');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-09-28 12:01:58.273674'),
(2,'auth','0001_initial','2023-09-28 12:01:58.555195'),
(3,'admin','0001_initial','2023-09-28 12:01:58.633301'),
(4,'admin','0002_logentry_remove_auto_add','2023-09-28 12:01:58.633301'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-09-28 12:01:58.633301'),
(6,'contenttypes','0002_remove_content_type_name','2023-09-28 12:01:58.664545'),
(7,'auth','0002_alter_permission_name_max_length','2023-09-28 12:01:58.695787'),
(8,'auth','0003_alter_user_email_max_length','2023-09-28 12:01:58.711408'),
(9,'auth','0004_alter_user_username_opts','2023-09-28 12:01:58.711408'),
(10,'auth','0005_alter_user_last_login_null','2023-09-28 12:01:58.727030'),
(11,'auth','0006_require_contenttypes_0002','2023-09-28 12:01:58.742651'),
(12,'auth','0007_alter_validators_add_error_messages','2023-09-28 12:01:58.742651'),
(13,'auth','0008_alter_user_username_max_length','2023-09-28 12:01:58.758276'),
(14,'auth','0009_alter_user_last_name_max_length','2023-09-28 12:01:58.773895'),
(15,'auth','0010_alter_group_name_max_length','2023-09-28 12:01:58.805136'),
(16,'auth','0011_update_proxy_permissions','2023-09-28 12:01:58.805136'),
(17,'auth','0012_alter_user_first_name_max_length','2023-09-28 12:01:58.820763'),
(18,'myapp','0001_initial','2023-09-28 12:01:59.070704'),
(19,'sessions','0001_initial','2023-09-28 12:01:59.086320'),
(20,'myapp','0002_trainer_photo','2023-10-03 06:08:38.628477'),
(21,'myapp','0003_posture_image_posture_title','2023-10-03 11:41:56.946445'),
(22,'myapp','0004_alter_posture_video','2023-10-03 11:49:39.589196'),
(23,'myapp','0005_alter_complaint_date_alter_feedback_date','2023-10-07 10:09:49.194096'),
(24,'myapp','0006_user_photo','2023-10-15 06:11:42.429982'),
(25,'myapp','0002_alter_payment_date','2023-10-17 07:04:47.255166'),
(26,'myapp','0003_payment_status','2023-10-17 07:16:55.624318'),
(27,'myapp','0002_alter_payment_status','2023-10-17 07:19:43.002114'),
(28,'myapp','0003_payment_date','2023-10-17 07:20:11.630973'),
(29,'myapp','0004_alter_payment_date','2023-10-17 07:40:23.270361'),
(30,'myapp','0005_chat','2023-10-17 08:02:09.664392'),
(31,'myapp','0006_rename_fromlogin_chat_from_rename_tologin_chat_to','2023-10-17 08:02:59.602207'),
(32,'myapp','0007_rename_from_chat_from_id_rename_to_chat_to_id','2023-10-17 08:03:26.389675');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('ompm4729fkut64ubr7gvwe8hde6dg05a','eyJsaWQiOjIzLCJ0b2xpZCI6IjIwIn0:1qsi6U:FhK4e8Ikk2-MFZZ_GZj2ikp7kF-5XjFpSHL9LYoJbps','2023-10-31 11:19:14.880156'),
('hbm5auh5jh58vrynai8mxbbocr2qx6gm','eyJsaWQiOjIwLCJ0b2xpZCI6IjIzIn0:1qsi3M:kcMkGLZv9k5W5d0XQm2pC-4Ojg1gW7zluL6z46Ti7Vo','2023-10-31 11:16:00.992967');

/*Table structure for table `myapp_category` */

DROP TABLE IF EXISTS `myapp_category`;

CREATE TABLE `myapp_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_category` */

insert  into `myapp_category`(`id`,`categoryname`) values 
(23,'Shoulder'),
(22,'Leg'),
(21,'Chest');

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `FROM_ID_id` bigint NOT NULL,
  `TO_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_FROMLOGIN_id_09fbf665` (`FROM_ID_id`),
  KEY `myapp_chat_TOLOGIN_id_e972e149` (`TO_ID_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_chat` */

insert  into `myapp_chat`(`id`,`message`,`date`,`FROM_ID_id`,`TO_ID_id`) values 
(1,'hiii','2023-10-17',1,1),
(2,'fdsfsdfsdf','2023-10-17',1,1),
(3,'jgggggg','2023-10-17',23,19),
(4,'jhhjgjhgj','2023-10-17',23,19),
(5,'hi','2023-10-17',19,23),
(6,'hello','2023-10-17',23,20),
(7,'kllllljjj','2023-10-17',23,19);

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_USER_id_21ed0b20` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1010 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`status`,`complaint`,`reply`,`date`,`USER_id`) values 
(1009,'replied','trainers are very bad','will improve','2023-10-16',11),
(1008,'replied','app is very good ','thankyou','2023-10-16',11);

/*Table structure for table `myapp_diet` */

DROP TABLE IF EXISTS `myapp_diet`;

CREATE TABLE `myapp_diet` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `file` varchar(500) NOT NULL,
  `TRAINER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_diet_TRAINER_id_583c9578` (`TRAINER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_diet` */

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_USER_id_fce7ccff` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`date`,`feedback`,`USER_id`) values 
(3,'2023-10-17','nice',10);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(20,'akk@gmail.com','2499','user'),
(23,'amith','123','trainer'),
(19,'akashmk1997@gmail.com','25290102','user'),
(1,'Akash','2499','Admin');

/*Table structure for table `myapp_payment` */

DROP TABLE IF EXISTS `myapp_payment`;

CREATE TABLE `myapp_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `acholdername` varchar(100) NOT NULL,
  `cvv` varchar(100) NOT NULL,
  `validity_date` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payment_USER_id_b93bd65c` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_payment` */

insert  into `myapp_payment`(`id`,`acholdername`,`cvv`,`validity_date`,`amount`,`USER_id`,`status`,`date`) values 
(1,'akash','2244','10/12/2025','500',10,'paid','2023-10-10');

/*Table structure for table `myapp_posture` */

DROP TABLE IF EXISTS `myapp_posture`;

CREATE TABLE `myapp_posture` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `video` varchar(100) NOT NULL,
  `CATEGORY_id` bigint NOT NULL,
  `TRAINER_id` bigint NOT NULL,
  `image` varchar(1000) NOT NULL,
  `title` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_posture_CATEGORY_id_23c610ec` (`CATEGORY_id`),
  KEY `myapp_posture_TRAINER_id_90d32d51` (`TRAINER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=586 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_posture` */

insert  into `myapp_posture`(`id`,`video`,`CATEGORY_id`,`TRAINER_id`,`image`,`title`) values 
(585,'/media/video20231017-155132.mp4',21,32,'/media/p220231017-155132.jpg','crossover'),
(583,'/media/video20231017-155028.mp4',22,32,'/media/p220231017-155028.jpg','press'),
(584,'/media/video20231017-155052.mp4',23,32,'/media/p220231017-155052.jpg','side raise');

/*Table structure for table `myapp_trainer` */

DROP TABLE IF EXISTS `myapp_trainer`;

CREATE TABLE `myapp_trainer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `certificate` varchar(500) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `photo` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_trainer_LOGIN_id_b7caa7db` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_trainer` */

insert  into `myapp_trainer`(`id`,`name`,`dob`,`gender`,`email`,`phone`,`place`,`certificate`,`LOGIN_id`,`photo`) values 
(32,'amith','2023-10-11','Male','amith','123','aaa','/media/p120231010/17/23-101034.jpg',23,'/media/p220231017-101034.jpg');

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `height` varchar(100) NOT NULL,
  `weight` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `photo` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`phone`,`email`,`height`,`weight`,`dob`,`gender`,`place`,`LOGIN_id`,`photo`) values 
(11,'akkuttan','1256387536','akk@gmail.com','165','70','2023-10-20','Male','kottooli',20,'/media/user20231016-215049.jpg'),
(10,'ajesh','7539518524','aj@gmail.com','172','80','2023-10-05','Male','kozhikode',19,'/media/user20231016-214629.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
