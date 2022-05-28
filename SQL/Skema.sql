-- Opretter anmodnings tabel
create table if not exists Skema (
ID int not null auto_increment, -- anmodningsID er en integer der tæller automatisk op
underviser varchar (50) null, -- accepterer strings på længden op til 50
kursus varchar (50) null, -- accepterer strings på længden op til 50
lokale varchar (50) null, -- accepterer lokalenavne med op til 50 karakterer
dato varchar (25) null, -- accepterer datoer som varchar med op til 25 karakterer
tid varchar (15) null, -- accepterer tidsrum som varchar med op til 15 karakterer
primary key (ID) -- den primære nøgle er ID
);

-- Indsætter 5 patienter i tabellen
INSERT INTO Skema (underviser,kursus,lokale,dato,tid)
VALUES
('Yaasir','Sygdomslære - Forelæsning','Aud. - Niels K. Jerne, Panum','30-06-2022','09:15-12:00'),
('Hugo','Systemudvikling - Theo execise','Und.lokale - A105, HCØ','30-06-2022','12:15-15:00'),
('Hugo','Systemudvikling - Lecture','Aud. - Lille UP1, DIKU','30-06-2022','13:15-17:00');

select * from Skema