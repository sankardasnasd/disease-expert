/*
SQLyog Community v13.1.9 (64 bit)
MySQL - 10.4.28-MariaDB : Database - dermacare
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dermacare` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `dermacare`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(25,'Can add diease',7,'add_diease'),
(26,'Can change diease',7,'change_diease'),
(27,'Can delete diease',7,'delete_diease'),
(28,'Can view diease',7,'view_diease'),
(29,'Can add doctor',8,'add_doctor'),
(30,'Can change doctor',8,'change_doctor'),
(31,'Can delete doctor',8,'delete_doctor'),
(32,'Can view doctor',8,'view_doctor'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add user',10,'add_user'),
(38,'Can change user',10,'change_user'),
(39,'Can delete user',10,'delete_user'),
(40,'Can view user',10,'view_user'),
(41,'Can add schedule',11,'add_schedule'),
(42,'Can change schedule',11,'change_schedule'),
(43,'Can delete schedule',11,'delete_schedule'),
(44,'Can view schedule',11,'view_schedule'),
(45,'Can add feedback',12,'add_feedback'),
(46,'Can change feedback',12,'change_feedback'),
(47,'Can delete feedback',12,'delete_feedback'),
(48,'Can view feedback',12,'view_feedback'),
(49,'Can add compliant',13,'add_compliant'),
(50,'Can change compliant',13,'change_compliant'),
(51,'Can delete compliant',13,'delete_compliant'),
(52,'Can view compliant',13,'view_compliant'),
(53,'Can add appointment',14,'add_appointment'),
(54,'Can change appointment',14,'change_appointment'),
(55,'Can delete appointment',14,'delete_appointment'),
(56,'Can view appointment',14,'view_appointment'),
(57,'Can add chat',15,'add_chat'),
(58,'Can change chat',15,'change_chat'),
(59,'Can delete chat',15,'delete_chat'),
(60,'Can view chat',15,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(14,'myapp','appointment'),
(15,'myapp','chat'),
(13,'myapp','compliant'),
(7,'myapp','diease'),
(8,'myapp','doctor'),
(12,'myapp','feedback'),
(9,'myapp','login'),
(11,'myapp','schedule'),
(10,'myapp','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-29 04:42:12.955399'),
(2,'auth','0001_initial','2023-10-29 04:42:13.269696'),
(3,'admin','0001_initial','2023-10-29 04:42:13.316593'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-29 04:42:13.332220'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-29 04:42:13.332220'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-29 04:42:13.379494'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-29 04:42:13.395138'),
(8,'auth','0003_alter_user_email_max_length','2023-10-29 04:42:13.410762'),
(9,'auth','0004_alter_user_username_opts','2023-10-29 04:42:13.426387'),
(10,'auth','0005_alter_user_last_login_null','2023-10-29 04:42:13.457633'),
(11,'auth','0006_require_contenttypes_0002','2023-10-29 04:42:13.457633'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-29 04:42:13.469151'),
(13,'auth','0008_alter_user_username_max_length','2023-10-29 04:42:13.473681'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-29 04:42:13.489349'),
(15,'auth','0010_alter_group_name_max_length','2023-10-29 04:42:13.504964'),
(16,'auth','0011_update_proxy_permissions','2023-10-29 04:42:13.504964'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-29 04:42:13.520585'),
(18,'myapp','0001_initial','2023-10-29 04:42:13.771864'),
(19,'sessions','0001_initial','2023-10-29 04:42:13.803125'),
(20,'myapp','0002_chat','2023-10-29 04:43:26.278644'),
(21,'myapp','0003_alter_appointment_date_alter_chat_date_and_more','2023-11-27 05:32:08.247954'),
(22,'myapp','0004_alter_appointment_time_alter_compliant_time_and_more','2023-11-27 05:35:38.751797');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('ly5fdo1a75pe9ale0iaz97ahns5ppqt0','eyJsaWQiOjF9:1r7TpT:AgWcbt0fkDf6O7Y4fdUP5SCPspOqQyuoAMTXDKC_dXE','2023-12-11 05:06:43.410221'),
('qdog7kb79ef0e5fw22cog19wiz3e3lfq','eyJsaWQiOjF9:1qwyMG:HjbP9LOYI3DTEcFUQ-HZ1u1d9ZEzpy0_CADEnIZFDvI','2023-11-12 05:29:08.230404');

/*Table structure for table `myapp_appointment` */

DROP TABLE IF EXISTS `myapp_appointment`;

CREATE TABLE `myapp_appointment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `SCHEDULE_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_appointment_SCHEDULE_id_e0e34324_fk_myapp_schedule_id` (`SCHEDULE_id`),
  KEY `myapp_appointment_USER_id_25c7e2d0_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_appointment_SCHEDULE_id_e0e34324_fk_myapp_schedule_id` FOREIGN KEY (`SCHEDULE_id`) REFERENCES `myapp_schedule` (`id`),
  CONSTRAINT `myapp_appointment_USER_id_25c7e2d0_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_appointment` */

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(100) NOT NULL,
  `FROMID_id` bigint(20) NOT NULL,
  `TOID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` (`FROMID_id`),
  KEY `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` (`TOID_id`),
  CONSTRAINT `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` FOREIGN KEY (`FROMID_id`) REFERENCES `myapp_login` (`id`),
  CONSTRAINT `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` FOREIGN KEY (`TOID_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_chat` */

/*Table structure for table `myapp_compliant` */

DROP TABLE IF EXISTS `myapp_compliant`;

CREATE TABLE `myapp_compliant` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complain` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_compliant_USER_id_2bdcc941_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_compliant_USER_id_2bdcc941_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_compliant` */

insert  into `myapp_compliant`(`id`,`complain`,`date`,`time`,`reply`,`status`,`USER_id`) values 
(1,'cccc','0000-00-00','00:00:00.000000','','',1),
(13,'trfgvhbjk','2023-11-27','12:45:00.000000','','pending',1);

/*Table structure for table `myapp_diease` */

DROP TABLE IF EXISTS `myapp_diease`;

CREATE TABLE `myapp_diease` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `dieasename` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `symtoms` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_diease` */

insert  into `myapp_diease`(`id`,`dieasename`,`details`,`symtoms`) values 
(1,'skin cancer','hkhlihlkgkuyliyhjgkugligliyg',''),
(2,'skin ca','',''),
(3,'skin cancer','uihuygyugyuguy','uhgyugyugyu'),
(4,'ewjfiowjfw fweklfnwieweflwenf','kciwijf','dnwekjdw'),
(5,'ewjfiowjfw fweklfnwieweflwenf','kciwijf','dnwekjdw'),
(6,'dfwdffwdf','wfwf','wfwefw');

/*Table structure for table `myapp_doctor` */

DROP TABLE IF EXISTS `myapp_doctor`;

CREATE TABLE `myapp_doctor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `photo` varchar(300) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `housename` varchar(100) NOT NULL,
  `houseno` varchar(100) NOT NULL,
  `mobileno` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_doctor_LOGIN_id_07e43244_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_doctor_LOGIN_id_07e43244_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_doctor` */

insert  into `myapp_doctor`(`id`,`name`,`place`,`age`,`gender`,`qualification`,`photo`,`pin`,`city`,`housename`,`houseno`,`mobileno`,`email`,`LOGIN_id`) values 
(1,'saikrishna','saikrishna','35','female','rtg','/media/20231127-103858.jpg','rgsg','rgsgs','gfgsrg','vzxzxvz','5545454','anudev@gmail.com',3),
(2,'saikrishna','saikrishna','35','male','rtg','/media/20231127-103954.jpg','rgsg','rgsgs','gfgsrg','vzxzxvz','5545454','anudev@gmail.com',4),
(3,'ytftyfc','jnkln','nkm','female','klnkllklnkl','/media/20231127-114323.jpg','nkl','nklkln','nklnl','klnnl','lnkl','klkln',5);

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feeedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `USERNAME_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_USERNAME_id_f7c4552c_fk_myapp_user_id` (`USERNAME_id`),
  CONSTRAINT `myapp_feedback_USERNAME_id_f7c4552c_fk_myapp_user_id` FOREIGN KEY (`USERNAME_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`feeedback`,`date`,`time`,`USERNAME_id`) values 
(3,'fdgsg','2023-11-27','02:55:00.000000',1);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'shibili','anudev','admin'),
(2,'hggg','ggg','user'),
(3,'anudev@gmail.com','111','doctor'),
(4,'anudev@gmail.com','12345678','doctor'),
(5,'klkln','12345678','doctor');

/*Table structure for table `myapp_schedule` */

DROP TABLE IF EXISTS `myapp_schedule`;

CREATE TABLE `myapp_schedule` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `DOCTOR_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_schedule_DOCTOR_id_1253d521_fk_myapp_doctor_id` (`DOCTOR_id`),
  CONSTRAINT `myapp_schedule_DOCTOR_id_1253d521_fk_myapp_doctor_id` FOREIGN KEY (`DOCTOR_id`) REFERENCES `myapp_doctor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_schedule` */

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `photo` varchar(300) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `housename` varchar(100) NOT NULL,
  `houseno` varchar(100) NOT NULL,
  `mobileno` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`place`,`age`,`gender`,`photo`,`pin`,`housename`,`houseno`,`mobileno`,`email`,`LOGIN_id`) values 
(1,'hhh','','','','','','','','','',2),
(5,'swds','sdsd','15','femaale','','673306','cdsa','25rd','9947245268','anudev@gmail.com',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
