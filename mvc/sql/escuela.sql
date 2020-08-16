

USE mm5gzlu0osfi6uv8;

CREATE TABLE alumnos(
    id_alumno int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    lastname2 varchar(50) NOT NULL,
    Matricula int(20) NOT NULL,
    Edad int(3) NOT NULL,
    Fecha date,
    Sexo varchar(20) NOT NULL,
    Estado varchar(20) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;


INSERT INTO alumnos(Nombre, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado)
values
('Julissa', 'Dominguez', 'Badillo', '1718110384', '20', '2000/04/05', 'Femenino', 'Soltera'),
('Andrea', 'Juarez', 'Munguia', '1718110394', '20', '2000/06/16', 'Femenino', 'Soltera');
