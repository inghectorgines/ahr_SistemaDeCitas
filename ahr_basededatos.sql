CREATE DATABASE IF NOT EXISTS ahr_citas;
USE ahr_citas;

CREATE TABLE doctores(
    id          int(25) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    consultorio int(25),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE citas(
    id           int(25) auto_increment not null,
    doctor_id    int(25) not null,
    paciente     varchar(255) not null,
    descripcion  MEDIUMTEXT,
    fecha        date not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_doctor FOREIGN KEY(doctor_id) REFERENCES doctores(id)
)ENGINE=InnoDb;