-- Opretter bruger tabel
create table if not exists Kurser (
ID int not null auto_increment, -- anmodningsID er en integer der tæller automatisk op
kursusnavn varchar (50) null, -- accepterer strings på længden op til 50
undervisningstype varchar (50) null, -- accepterer strings på længden op til 50
underviserID int (25) null, -- accepterer datoer som varchar med op til 25 karakterer
primary key (ID), -- den primære nøgle er ID
FOREIGN KEY (underviserID) REFERENCES Bruger(ID)
);

-- Indsætter 5 patienter i tabellen
INSERT INTO Kurser (kursusnavn,undervisningstype,underviserID)
VALUES
('Systemudvikling','Theo execise',1),
('Systemudvikling','Lecture',1),
('Sygdomslære', 'Forelæsning',2)
;

select* from Kurser