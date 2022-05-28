-- Opretter anmodnings tabel
create table if not exists Anmodninger (
ID int not null auto_increment, -- anmodningsID er en integer der tæller automatisk op
underviser varchar (50) null, -- accepterer strings på længden op til 50
kursus varchar (50) null, -- accepterer strings på længden op til 50
dato varchar (25) null, -- accepterer datoer som varchar med op til 25 karakterer
tid varchar (15) null, -- accepterer tidsrum som varchar med op til 15 karakterer
primary key (ID) -- den primære nøgle er ID
);

-- Indsætter 5 patienter i tabellen
INSERT INTO Anmodninger (underviser,kursus,dato,tid)
VALUES
('Hugo','Systemudvikling - Theo execise','24-06-2022','09:00-12:00'),
('Hugo','Systemudvikling - Lecture','26-06-2022','15:00-17:00'),
('Yaasir','Sygdomslære - Forelæsning','27-06-2022','09:00-12:00');


select* from Anmodninger
